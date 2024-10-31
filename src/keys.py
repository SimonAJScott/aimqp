from enum import Enum
from pynput.keyboard import Key
import pyautogui
import time


class Keys(Enum):
    UP = Key.up         # Move up (on walls?)
    DOWN = Key.down     # Move down
    LEFT = Key.left     # Move left
    RIGHT = Key.right    # Move right
    JUMP = 'c'     # Jump
    DASH = 'x'           # Dash
    GRAB = 'z'  # Grab
    # TALK = 'x'      # Interact (or whatever key you have mapped)
    # MENU = 'esc'        # Open menu

    def press(self):
        """Press the key associated with this enum member using pyautogui."""
        pyautogui.keyDown(self.value)  # Press down the key
        time.sleep(0.1)  # Hold for a brief moment
        pyautogui.keyUp(self.value)    # Release the key
