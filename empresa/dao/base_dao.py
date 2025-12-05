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
     
    # Create - inaerir valores na tabela
     
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
        
    # Update - o que tanto?
    def update(self, pk: str, value: T, model: T) -> bool: # bool = retorna verdadeiro ou falso
        try:
            data_dict = self.to_dict(model) #converte o modelo em dicionário
            response = self._client.table(self._table_name).update(data_dict).eq(pk, value).execute() # eq = onde pk = value, atualize com data_dict
            return response.status_code == 200 #retorna True se a atualização foi bem-sucedida
        except Exception as e:
            print(f'Erro ao atualizar registro: {e}')
            return False
     
    # Delete
    
    