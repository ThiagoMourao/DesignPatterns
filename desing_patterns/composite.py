from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class BoxStructure(ABC):
    """Component"""
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass

    def remove(self, child: BoxStructure) -> None: pass

class Box(BoxStructure):
    """Composite""" 
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n {self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)

class Product(BoxStructure):
    """Leaf"""
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
    
    def print_content(self) -> None:
        print(f'   {self.name}, {self.price}')

    def get_price(self) -> float:
        return self.price
