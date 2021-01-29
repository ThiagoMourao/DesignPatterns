from __future__ import annotations
from abc import ABC, abstractmethod

class Order:
    def __init__(self, total: float, discount: DiscountStrategy = None):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total
    
    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)
    

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass

class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value*0.2)

class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value*0.5)

class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value

class CustomDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)
