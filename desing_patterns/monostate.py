'''utiliza objetos diferentes porem com os mesmos atributos e valores dos mesmos, melhor que o singleton para utilizar com herança'''
class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={x}' for k, x in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()

class MonoState(StringReprMixin):
    _state = {}

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome