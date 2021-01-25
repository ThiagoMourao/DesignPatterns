from random import choice
from desing_patterns.Simple_factory import VeiculoFactory


carros_disponiveis = ['luxo', 'popular']

for i in range(10):  
    carro = VeiculoFactory(choice(carros_disponiveis))
    carro.buscar_cliente()
