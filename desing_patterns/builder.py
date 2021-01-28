from abc import ABC, abstractmethod
from desing_patterns.monostate import StringReprMixin

#Product
class User(StringReprMixin):
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []

#Builder
class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstName(self, firstname): pass

    @abstractmethod
    def add_lastName(self, lastName): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone_numbers): pass

    @abstractmethod
    def add_address(self, addresses): pass

#ConcreateBuilder
class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    '''Setter, salva o objeto anterior e criar um novo resetado no "reset" '''
    @property
    def result(self): 
        return_data = self._result
        self.reset() # new user
        return return_data

    def add_firstName(self, firstname):
        self._result.firstName = firstname
        return self

    def add_lastName(self, lastName):
        self._result.lastName = lastName
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone_numbers):
        self._result.phone_numbers.append(phone_numbers)
        return self

    def add_address(self, addresses):
        self._result.addresses.append(addresses)
        return self

class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_firstName(firstname).add_lastName(lastname)
        self._builder.add_age(age)
        return self._builder.result

    def with_address(self, firstname, lastname, address):
        self._builder.add_firstName(firstname)        
        self._builder.add_address(address).add_lastName(lastname)
        return self._builder.result
