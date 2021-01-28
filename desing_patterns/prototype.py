from __future__ import annotations
from typing import List
from copy import deepcopy
from desing_patterns.monostate import StringReprMixin

class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self):
        return deepcopy(self)

    
class Address(StringReprMixin):
    def __init__(self, street: str, number : str) -> None:
        self.street = street
        self.number = number