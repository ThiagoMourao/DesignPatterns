from random import choice
from desing_patterns.Simple_factory import VeiculoFactory
from desing_patterns.factory_method import ZonaNorteVeiculoFactory, ZonaSulVeiculoFactory

class testes:
        
    def simple_factory(self):  

        for i in range(10):  
            carro = VeiculoFactory(choice(VeiculoFactory.carros_disponiveis))
            carro.buscar_cliente()

    def factory_method(self):
        print('ZONA NORTE:')
        for i in range(10):  
            carro = ZonaNorteVeiculoFactory(choice(ZonaNorteVeiculoFactory.veiculos_disponiveis))
            carro.buscar_cliente()

        print('\nZONA SUL:')
        for i in range(10):  
            carro = ZonaSulVeiculoFactory(choice(ZonaSulVeiculoFactory.veiculos_disponiveis))
            carro.buscar_cliente()