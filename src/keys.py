from enum import Enum
from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()


class Keys(Enum):
    UP = Key.up         # Move up (on walls?)
    DOWN = Key.down     # Move down
    LEFT = Key.left     # Move left
    RIGHT = Key.right    # Move right
    JUMP = 'c'     # Jump
    DASH = 'x'           # Dash
    GRAB = 'z'  # Grab

    def press(self):
        """
        presses said button for x seconds
        """
        keyboard.press(self.value)
        time.sleep(0.1)
        keyboard.release(self.value)


def randomButtons(duration):
    """
        presses random buttons for x seconds
        """
    start_time = time.time()  # Record the start time
    end_time = start_time + duration  # Run for duration seconds

    while time.time() < end_time:
        key_to_press = random.choice(list(Keys))  # Randomly choose a key
        # Print which key is being pressed
        print(f"Pressing {key_to_press.name}")
        key_to_press.press()  # Press the randomly selected key
        time.sleep(0.2)  # Sleep for half a second between presses
