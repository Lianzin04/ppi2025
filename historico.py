import datetime   #pegar data da craicção

class Historico:
    def __init__(self):
      self.data_abertura = datetime.datetime.today()
      self.trasacoes = [] #lista de transações

    def imprime(self):
      print(f'Data abertura: {self.data_abertura}')
      print('trasaco:')
      for t in self.trasacoes:
         print('-', t)
