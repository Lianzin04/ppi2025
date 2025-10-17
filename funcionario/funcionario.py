class Funcionario:

    _slot_ = ['_nome', '_cpf', '_salario'] # expecifica os atributos que a classe podem ser acessados

    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

        def get_bonificacao(self):
            return self.salario * 0.1 
        
        def __str__(self):
            return f'Nome: {self.nome}, CPF: {self.cpf}, Salário: {self.salario:2f}'

        @property #permite acessar o atributo como se fosse um atributo normal
        def nome(self):
            return self._nome
        @nome.setter #permite modificar o atributo como se fosse um atributo normal
        def nome(self, nome):
            self._nome = nome

        @property  
        def cpf(self):  
            return self._cpf
        
        @cpf.setter
        def cpf(self, cpf):
            self._cpf = cpf

        @property
        def salario(self):
            return self._salario
        
        @salario.setter
        def salario(self, salario):
            self._salario = salario