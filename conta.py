# 19/09
class Conta:
     def __init__(self, titular, agencia, numero, pix, saldo):
          self.titular = titular
          self.agencia = agencia
          self.numero = numero
          self.pix = pix
          self.saldo = saldo

          def deposita(self, valor):
               self.saldo += valor

          def saca(self, valor):
              self. saldo -= valor
                
          def extrato(self, valor):
              self. saldo -= valor

          print(f'Titular': {self.titular}\ {})

          def trafere(self, destino, valor):
           if(self.saca(valor)):
              destino.deposita(valor)
              return True
           else:
               return False

