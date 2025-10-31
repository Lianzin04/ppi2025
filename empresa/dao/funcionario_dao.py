from supabase import Client
from empresa.dao.base_dao import BaseDAO
from empresa.models import funcionario

class FuncionarioDAO(BaseDAO[funcionario]):
    def __init__(self, client: Client):
        super().__init__(client, 'funcionario') # nome da tabela no supabase
       
    def to_model(self, data: dict) -> funcionario:
        return funcionario.from_dict(data)  
        