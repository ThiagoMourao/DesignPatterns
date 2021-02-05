from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List
from copy import deepcopy

class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name, value):
        raise AttributeError('Sorry, I am immutable')

class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

class Caretaker:
    def __init__ (self, originator: ImageEditor):
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())