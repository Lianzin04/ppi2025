'''
baseDAO
Classe abstrata para os DAOs(Data Access Objects)'''


from abc import ABC, abstractmethod # pq usar o abstractmethod?  OBRIGAR A IMPLEMENTAÇÃO DE MÉTODOS NAS CLASSES FILHAS
from typing import List, Optional,TypeVar, Generic
from supabase import Client

# Typevar - torna a classe genérica
T = TypeVar('T') # Tipo genérico para as entidades

class BaseDAO(ABC, Generic[T]):
    
    def __init__(self, client: Client, table_name: str): # passar uma instância do supabase client
        self._client = client
        self._table_name = table_name
        
        # dic -> model | model -> dic

    @abstractmethod #seu filho é obrigado a implementar esse método
    def to_model(self, data: dict) -> T:
        pass
    
    @abstractmethod
    def to_dict(self, model: T) -> dict:
        pass
    
    # Fazer o CRUD
     
    # Create 
    def create(self, obj: T) -> Optional[T]:
        try:
            data = self.to_dict(obj)  # usa o conversor da subclasse para obter um dict serializável
            response = self._client.table(self._table_name).insert(data).execute() # insere o dicionário na tabela
            if response.data and len(response.data) > 0: #verifica se há dados na resposta
                return self.to_model(response.data[0]) #retorna o primeiro registro inserido como um modelo
            return None 
        except Exception as e:
            print(f"Erro ao criar registro: {e}")
            return None
     
    # Read 
    def read(self, pk: str, value: T) -> Optional[T]: # optional = pode retornar um valor ou None
        try:
            response = self._client.table(self._table_name).select('*').eq(pk, value).execute() # eq = igual. tipo: pegue todos os registros onde pk = value
            if response.data and len(response.data) > 0: #verifica se há dados na resposta
                return self.to_model(response.data[0]) #retorna o primeiro registro encontrado
            return None #nenhum registro encontrado
        except Exception as e: #trata qualquer exceção que possa ocorrer durante a operação
            print(f'Erro ao buscar registro: {e}') #mensagem de erro
            return [] # retorna uma lista vazia em caso de erro
        
    # - retorna todos os valores da tabela
    def read_all(self) -> List[T]:
        try:
            response = self._client.table(self._table_name).select('*').execute()
            if response.data:
                return [self.to_model(item) for item in response.data] #converter cada dicionário em um modelo
            return []
        except Exception as e:
            print(f'Erro ao buascar todos os registros: {e}')
            return []
        
    # Update 
    def update(self, pk: str, value: str, obj: T) -> Optional[T]: #pk = nome do campo da chave primária | value = valor da chave primária | obj = objeto com os novos dados
        try:
            data = self.to_dict(obj)    #converte o objeto em um dicionário serializável
            response = self._client.table(self._table_name).update(data).eq(pk, value).execute() #atualiza o registro onde pk = value
            if response.data and len(response.data) > 0: # verifica se há dados na resposta
                return self.to_model(response.data[0]) #retorna o registro atualizado como um modelo
            return None #nenhum registro atualizado
        except Exception as e: #
            print(f'Erro ao atualizar registro: {e}')
            return None
     
    # Delete
    def delete(self, pk: str, value: str) -> bool: #pk = nome do campo da chave primária | value = valor da chave primária
        try:
            response = self._client.table(self._table_name).delete().eq(pk, value).execute() #deleta o registro onde pk = value
            return len(response.data) > 0 #retorna True se algum registro foi deletado
        except Exception as e:  # trata qualquer exceção que possa ocorrer durante a operação
            print(f'Erro ao deletar registro: {e}') #mensagem de erro
            return False #retorna False em caso de erro
    
    