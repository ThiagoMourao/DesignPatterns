from random import choice
from desing_patterns.Simple_factory import VeiculoFactory
from desing_patterns.factory_method import ZonaNorteVeiculoFactory, ZonaSulVeiculoFactory
from desing_patterns.abstract_method import Filiais
from desing_patterns.singleton import AppSettings, AppSettings2, AppSettings3
from desing_patterns.monostate import MonoState
from desing_patterns.builder import UserDirector, UserBuilder
from desing_patterns.prototype import Person, Address
from desing_patterns.strategy import Order, TwentyPercent,FiftyPercent, NoDiscount, CustomDiscount
from desing_patterns.observer import WeatherStation, Smartphone, Notebook
from desing_patterns.command import RemoteController, LightOnCommand, Light, LightChangeColor
from desing_patterns.template_method import StylishPizza, ChocolatePizza
from desing_patterns.chain_responsibility import HandlerABC, HandlerDEF, HandlerUnsolved
from desing_patterns.state import Orderr

class tests:
        
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

    def strategy(self):
        twenty_percent = TwentyPercent()
        order = Order(1000, twenty_percent)
        print(order.total, order.total_with_discount)
        
        fifty_percent = FiftyPercent()
        order2 = Order(2000, fifty_percent)
        print(order2.total, order2.total_with_discount)

        no_discount = NoDiscount()
        order3 = Order(2000, no_discount)
        print(order3.total, order3.total_with_discount)

        order4 = Order(10000, CustomDiscount(35.0))
        print(order4.total, order4.total_with_discount)

    def observer(self):
        weather_station = WeatherStation()

        smartphone = Smartphone('iPhone', weather_station)
        other_smartphone = Smartphone('Android', weather_station)
        notebook = Notebook('Dell', weather_station)

        weather_station.add_observer(smartphone)
        weather_station.add_observer(other_smartphone)
        weather_station.add_observer(notebook)

        weather_station.state = {'temperature': '30'}

        weather_station.state = {'temperature': '32', 'humidity': '90'} 

        weather_station.state = {'thermal_sensation': '36'}

        weather_station.remove_observer(other_smartphone)
        weather_station.reset_state()

    def command(self):
        bedroom_light = Light('Red', 'bedroom')

        bedroom_light_on = LightOnCommand(bedroom_light)
        bedroom_light_blue = LightChangeColor(bedroom_light, 'blue')
        bedroom_light_red = LightChangeColor(bedroom_light, 'red')

        remote = RemoteController()
        remote.button_add_command('first_button', bedroom_light_on)
        remote.button_add_command('second_button', bedroom_light_blue)
        remote.button_add_command('third_button', bedroom_light_red)

        remote.button_pressed('first_button')
        remote.button_pressed_again('first_button')
        
        remote.button_pressed('second_button')
        remote.button_pressed_again('second_button')

        remote.button_pressed('third_button')
        remote.button_pressed_again('third_button')

        print()
        remote.global_undo()

    def template_method(self):
        pizza1 = StylishPizza()
        pizza1.prepare()
        print()
        pizza2 = ChocolatePizza()
        pizza2.prepare()

    def chain_of_responsibility(self):
        handler_unsolved = HandlerUnsolved()
        handler_def = HandlerDEF(handler_unsolved)
        handler_abc = HandlerABC(handler_def)

        print(handler_abc.handle('B'))

    def state(self):
        order = Orderr()
        order.reject()
        order.reject()
        

