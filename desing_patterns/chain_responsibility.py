from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> None: pass

class HandlerABC(Handler):
    def __init__(self, sucessor: Handler):
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'HandlerABC: conseguiu tratar o valor {letter}'
        return self.sucessor.handle(letter)

class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler):
        self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'HandlerDEF: conseguiu tratar o valor {letter}'
        return self.sucessor.handle(letter)

class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'Não conseguiu tratar {letter}'
        

