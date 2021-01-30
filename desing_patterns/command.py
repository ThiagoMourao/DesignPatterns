from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

class Light:
    """Receiver - Smart Light """
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'Light {self.name} in {self.room_name} in now ON')

    def off(self) -> None:
        print(f'Light {self.name} in {self.room_name} in now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'Light {self.name} in {self.room_name} in now color {self.color}')

class ICommand(ABC):
    """Command of Interface """
    @abstractmethod
    def pressed(self) -> None: pass

    @abstractmethod
    def pressed_again(self) -> None: pass

class LightOnCommand(ICommand):
    """Concreate Command """
    def __init__(self, light: Light) -> None:
        self.light = light

    def pressed(self) -> None:
        self.light.on()

    def pressed_again(self) -> None:
        self.light.off()

class LightChangeColor(ICommand):
    """Concreate Command """
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def pressed(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def pressed_again(self) -> None:
        self.light.change_color(self._old_color)

class RemoteController:
    """Invoker"""
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, button_name: str, command: ICommand) -> None:
        self._buttons[button_name] = command

    def button_pressed(self, button_name: str) -> None:
        if button_name in self._buttons:
            self._buttons[button_name].pressed()
            self._undos.append((button_name, 'execute'))
        
    def button_pressed_again(self, button_name: str) -> None:
        if button_name in self._buttons:
            self._buttons[button_name].pressed_again()
            self._undos.append((button_name, 'undo'))

    def global_undo(self):
        if not self._undos:
            return None

        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].pressed()
        else:
            self._buttons[button_name].pressed_again()   

        self._undos.pop()