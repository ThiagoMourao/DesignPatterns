# UBER
from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):  # Product
    @abstractmethod 
    def buscar_cliente(self) -> None: pass

class VeiculoPopular(ABC):  # Product
    @abstractmethod 
    def buscar_cliente(self) -> None: pass
 
class CarroLuxoZN(VeiculoLuxo):  # ConcreteProduct1
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN está buscando clientes...')

class CarroPopularZN(VeiculoPopular):  # ConcreteProduct2
    def buscar_cliente(self) -> None:
        print('Carro popular ZN está buscando clientes...')

class MotoZN(VeiculoPopular):  # ConcreteProduct3
    def buscar_cliente(self) -> None:
        print('Moto ZN está buscando clientes...')

class MotoLuxoZN(VeiculoLuxo):  # ConcreteProduct4
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZN está buscando clientes...')

class CarroLuxoZS(VeiculoLuxo):  # ConcreteProduct1-1
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS está buscando clientes...')

class CarroPopularZS(VeiculoPopular):  # ConcreteProduct2-1
    def buscar_cliente(self) -> None:
        print('Carro popular ZS está buscando clientes...')

class MotoZS(VeiculoPopular):  # ConcreteProduct3-1
    def buscar_cliente(self) -> None:
        print('Moto ZS está buscando clientes...')

class MotoLuxoZS(VeiculoLuxo):  # ConcreteProduct4-1
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS está buscando clientes...')

class VeiculoFactory(ABC):  # Creator
    @abstractmethod
    def get_carro_luxo(self) -> VeiculoLuxo: pass

    @abstractmethod
    def get_carro_popular(self) -> VeiculoPopular: pass

    @abstractmethod
    def get_moto_luxo(self) -> VeiculoLuxo: pass

    @abstractmethod
    def get_moto_popular(self) -> VeiculoPopular: pass
 

class ZonaNorteVeiculoFactory(VeiculoFactory): #Concreate Creator1
    
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoZN()

class ZonaSulVeiculoFactory(VeiculoFactory): #Concreate Creator2
        
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoZS()

class Filiais:
    def buscar_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            luxo_luxo = factory.get_moto_luxo()
            luxo_luxo.buscar_cliente()

