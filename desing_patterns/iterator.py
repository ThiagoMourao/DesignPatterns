from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable
from typing import List, Any

class MyIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = 0
    
    def __next__(self) -> List[Any]:
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = -1
    
    def __next__(self) -> List[Any]:
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration

class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items) #
    
    def __iter__(self) -> None:
        return MyIterator(self._items)

    def reverse_iterator(self):
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'

    def add(self, value) -> None:
        self._items.append(value)
