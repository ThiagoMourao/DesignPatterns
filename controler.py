from random import choice
from desing_patterns.Simple_factory import VeiculoFactory
from desing_patterns.factory_method import ZonaNorteVeiculoFactory, ZonaSulVeiculoFactory
from desing_patterns.abstract_method import Filiais
from desing_patterns.singleton import AppSettings, AppSettings2, AppSettings3
from desing_patterns.monostate import MonoState
from desing_patterns.builder import UserDirector, UserBuilder
from desing_patterns.prototype import Person, Address

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

    def abstract_method(self):
        cliente = Filiais()
        cliente.buscar_clientes()

    def singleton(self):
        App1 = AppSettings()
        App2 = AppSettings()

        print(f'{App1} \n{App2}')

    def singleton_decorator(self):
        App1 = AppSettings2()
        App1.tema = 'O tema claro'
        print(App1.tema)

        App2 = AppSettings2()
        print(App2.tema)
    
    def singleton_metaclass(self):
        App1 = AppSettings3()
        App1.tema = 'O tema claro'
        print(App1.tema)

        App2 = AppSettings3()
        print(App2.tema)

    def monoState(self):
        m = MonoState(nome='Thiago')
        m2 = MonoState(sobrenome='Mourao')
        
        print(m)
        print(m2)
        print(m == m2)

    def builder(self):
       user_builder = UserBuilder()
       user_director = UserDirector(user_builder)
       user1 = user_director.with_age('Thiago', 'Mourao', 23)
       print(user1)

       user2 = user_director.with_address('Thiago', 'Mourao', 'Av. Primeiro de Junho')
       print(user2)

    def prototype(self):
        thiago = Person('Thiago', 'Mourao')
        adress_thiago = Address('Av. Primeiro de Junho', '345B')
        thiago.add_address(adress_thiago)
        
        wife_thiago = thiago.clone()
        wife_thiago.firstname = 'Mary'

        print(thiago)
        print(wife_thiago)