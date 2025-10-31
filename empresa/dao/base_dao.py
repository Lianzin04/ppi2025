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
    
    # CRUD
     
    # Create
     
    # Read - retorna todos os valores da tabela
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
     
    # Delete
    
    