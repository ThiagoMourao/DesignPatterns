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

class Moto(Veiculo):  # ConcreteProduct3
    def buscar_cliente(self) -> None:
        print('Moto está buscando clientes...')

class MotoLuxo(Veiculo):  # ConcreteProduct4
    def buscar_cliente(self) -> None:
        print('Moto de luxo está buscando clientes...')

class VeiculoFactory(ABC):  # Creator
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @abstractmethod
    def get_carro(self, tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory): #Concreate Creator1
    veiculos_disponiveis = ['luxo', 'popular', 'moto', 'moto_luxo']
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veículo não existe'

class ZonaSulVeiculoFactory(VeiculoFactory): #Concreate Creator2
    veiculos_disponiveis = ['luxo', 'popular']
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()        
        assert 0, 'Veículo não existe'

