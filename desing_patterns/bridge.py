from __future__ import annotations
from abc import ABC, abstractmethod

class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: pass

    @abstractmethod
    def decrease_volume(self) -> None: pass

    @abstractmethod
    def power(self) -> None: pass

class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device
    
    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power

class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, volume: int) -> None: pass

    @property
    @abstractmethod
    def power(self) -> bool: pass

    @power.setter
    def power(self, power: bool) -> None: pass

class TV(IDevice):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = __class__.__name__


    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self.power:
            print(f'Please, turn {self._name} ON')
            return

        if volume > 100:
            return
        if volume < 0:
            return

        self._volume = volume
        print(f'Volume was increamented to {self._volume}')

    @property
    def power(self) -> bool:
        return self._power        

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power
        power_status = 'ON' if self._power else 'OFF'
        
        print(f'{self._name} is now {power_status}')

