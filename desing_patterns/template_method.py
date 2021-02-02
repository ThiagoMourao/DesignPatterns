from abc import ABC, abstractmethod

class Pizza(ABC):
    """Class Abstract"""
    def prepare(self) -> None:
        """Template Method"""
        self.hook()
        self.add_ingrentients()        
        self.cook()
        self.cut()
        self.serve()    

    def hook(self) -> None: pass

    @abstractmethod
    def add_ingrentients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass

    def cut(self) -> None: 
        print(f'{self.__class__.__name__}: Cutting Pizza')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Serving Pizza')

class StylishPizza(Pizza):
    def add_ingrentients(self) -> None:
        print('Adding ham, cheese and peperone')

    def cook(self) -> None:
        print('Cooking for 45 min in oven')

class ChocolatePizza(Pizza):
    def hook(self) -> None:
        print('Checking for nutela')

    def add_ingrentients(self) -> None:
        print('Adding chocolate, ham and nutela')

    def cook(self) -> None:
        print('Cooking for 25 min in oven')


