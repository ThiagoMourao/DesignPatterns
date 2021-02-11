from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict

class Client:
    """Context"""
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        #Extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)

class Address:
    """Flyweigh"""
    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, address_details, self._zip_code 
        )

class AddressFactory:
    _addresses : Dict = {}

    def _get_key(self, **kwargs):
        return ''.join(kwargs.values())

    def get_address(self, **kwargs):
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Using object already created')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Creating new object')

        return address_flyweight