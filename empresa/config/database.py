# importar os módulos necessários para a conexão com o Supabase
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class SupabaseConnection:
    '''' 
    Padrão de projeto - Singçeton 
    Garante apenas uma instância em toda a aplicação
    '''
    _instance = None
    #type Hint - ganrante o tipo de dado ser atribuído a um atributo

    _client: Client = None #no momento ele não existe

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SupabaseConnection, cls).__new__(cls) #criando uma instância
            cls._instance._init_connection() #inicializa a conexão
        return cls._instance
    
    def _init_connection(self): # inicializa a conexão com o Supabase
        SUPABASE_URL = os.getenv("SUPABASE_URL") # os = serve para acessar variaveis de ambiente
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")


        if not SUPABASE_URL or not SUPABASE_KEY:
            raise ValueError("ERRO❌❌❌ As variáveis de ambiente SUPABASE_URL e SUPABASE_KEY devem ser definidas.") # raiser = lança uma exceção(um erro)
        
        self._client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("Conexão com Supabase show ✅.")

        @property
        def client(self) -> Client: #type Hint
            return self._client

        
            