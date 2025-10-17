from abc import ABC, abstractmethod

class Pessoa(ABC):
    __slots__ = ['_nome', '_cpf']

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def __str__(self):
        return f'Nome: {self._nome}, CPF: {self._cpf}'


