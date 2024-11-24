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


class Actions:
    """
    A class to input in-game actions. (can add more later)
    """

    @staticmethod
    def press(key, duration):
        """
        presses said button for a certain duration, then lifts

        :param key: must input key enum to work
        :param duration: Time in seconds to hold down button
        """
        keyboard.press(key.value)
        time.sleep(duration)
        keyboard.release(key.value)

    @staticmethod
    def randomButtons(duration=1, wait=0.2):
        """
        Presses random buttons (did not implement multiple buttons, can change later)

        :param duration: Time in seconds to hold the key
        :param wait: Time to wait between each press
        """
        start_time = time.time()  # Record the start time
        end_time = start_time + duration  # Run for duration seconds

        while time.time() < end_time:
            key_to_press = random.choice(list(Keys))  # Randomly choose a key
            # Print which key is being pressed
            print(f"Pressing {key_to_press.name}")
            # Press the randomly selected key
            Actions.press(key_to_press, duration)
            time.sleep(wait)  # Sleep for half a second between presses
