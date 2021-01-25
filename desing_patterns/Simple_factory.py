# UBER
from abc import ABC, abstractmethod


class Veiculo(ABC):  # Product
    @abstractmethod 
    def buscar_cliente(self) -> None: pass
 
class CarroLuxo(Veiculo):  # ConcreteProduct1
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando clientes...')

class CarroPopular(Veiculo):  # ConcreteProduct2
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando clientes...')

class VeiculoFactory:  # Factory
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe'

    def buscar_cliente(self):
        self.carro.buscar_cliente()
