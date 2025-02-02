from pynput.keyboard import Key
from enum import Enum


class Keys(Enum):
    LEFT = Key.left
    RIGHT = Key.right
    JUMP = Key.space
    DASH = Key.shift
    DOWN = Key.down
