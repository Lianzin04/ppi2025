from historico import Historico

class Conta:
    def __init__(self, cliente, agencia, numero, pix, saldo): #construtor(metodod da propria instancia)
        self.cliente = cliente #usado para agreagar
        self.agencia = agencia
        self.numero = numero
        self.pix = pix
        self._saldo = saldo
        self.historico = Historico() #composicao

        #tecnica chamada ?
    def deposita(self, valor):
        self.saldo += valor
        self.historico.trasacoes.append(f'Deposito de R$:{valor:.2f}')

    def saca(self, valor):
        if(self.saldo < valor):
            self.historico.trasacoes.append(f'Saldo insuficiente. Valor {valor:.2f}. Saldo {self.saldo}')
            return False
        else:
            self.saldo -= valor
            return True
    
    def extrato(self):
        self.historico.trasacoes.append(f'Extrato. saldo {self.saldo:.2f}')
        print(f'Titular: {self.cliente.nome}\nCPF: {self.cliente.cpf}\nAgência: {self.agencia}\nNúmero: {self.numero}\nPIX: {self.pix}\nSaldo: {self.saldo:.2f}\n')

    def transfere(self, destino, valor):
        self.historico.trasacoes.append(f'trasfe(destino.cliente)')
        if(self.saca(valor)):
            destino.deposita(valor)
            return True
        else:
            return False