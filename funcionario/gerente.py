from funcionario.funcionario import Funcionario

class Gerente(Funcionario):

    _slot_ = ['_nome', '_cpf', '_salario', '_senha', '_qtd_gerenciaveis']

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario) #chama o construtor da classe mãe
        self.senha = senha
        self.qtd_gerenciaveis = qtd_gerenciaveis

    @property
    def senha(self):
        return self._senha
    @senha.setter   
    def senha(self, senha):
        self._senha = senha

    @property
    def qtd_gerenciaveis(self):
        return self._qtd_gerenciaveis
    @qtd_gerenciaveis.setter
    def qtd_gerenciaveis(self, qtd):
        self._qtd_gerenciaveis = qtd



