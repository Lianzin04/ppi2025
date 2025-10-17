class ControleDeBonificacao:

    def registra(self, obj):
        if(isinstance(obj, Funcionario)):
           self._total += obj.get_bonificacao()


