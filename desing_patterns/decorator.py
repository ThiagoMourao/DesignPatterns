from __future__ import annotations
from dataclasses import dataclass
from typing import List
from copy import deepcopy

@dataclass
class Ingredient:
    price: float

@dataclass
class Bread(Ingredient):
    price: float = 1.5

@dataclass
class Sausage(Ingredient):
    price: float = 4.99

@dataclass
class Bacon(Ingredient):
    price: float = 7.99

@dataclass
class Egg(Ingredient):
    price: float = 1.5

@dataclass
class Cheese(Ingredient):
    price: float = 6.35

@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25

@dataclass
class PotatoesSticks(Ingredient):
    price: float = 0.99

class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            Ingredient.price for Ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name} ({self.price}) -> {self.ingredients}'

class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients : List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoesSticks()
        ]

class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        self._ingredients : List[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoesSticks()
        ]

#Decorators
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog)-> None:
        self._hotdog = hotdog
    

    @property
    def price(self) -> float:
        self._hotdog.price

    @property
    def name(self) -> str:
        return self._hotdog._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._hotdog._ingredients

class BaconDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog)-> None:
        super().__init__(hotdog)

        self._ingredient = Bacon()
        self._ingredients = deepcopy(self._hotdog._ingredients)
        self._ingredients.append(self._ingredient)
    
    @property
    def price(self) -> float:
        return round(sum([
            Ingredient.price for Ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return f'{self._hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients


class HotdogDecoratorAbstract(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient)-> None:
        self._hotdog = hotdog
        self._ingredient = ingredient

        self._ingredients = deepcopy(self._hotdog.ingredients)
        self._ingredients.append(self._ingredient)
    
    @property
    def name(self) -> str:
        return f'{self._hotdog.name} + {self._ingredient.__class__.__name__}'



