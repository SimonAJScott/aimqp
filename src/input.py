from enum import Enum
from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()
pressed_keys = set()


class Keys(Enum):
    UP = Key.up         # Move up (on walls?)
    DOWN = Key.down     # Move down
    LEFT = Key.left     # Move left
    RIGHT = Key.right    # Move right
    JUMP = 'c'     # Jump
    DASH = 'x'           # Dash
    GRAB = 'z'  # Grab

    def getKeys(cls):
        return {key.value for key in cls}


class Actions:
    """
    A class to input in-game actions. (can add more later)
    """

    def on_press(key):
        """
        helper for listener
        """
        if (key in Keys.getKeys()):
            pressed_keys.add(key)

    def on_release(key):
        """
        helper for listener
        """
        if (key in pressed_keys):
            pressed_keys.discard(key)

    # Listener setup
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

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
    def pushDownKey(key):
        """
        presses said button

        :param key: must input key enum to work
        """
        keyboard.press(key.value)

    @staticmethod
    def liftKey(key):
        """
        releases said button

        :param key: must input key enum to work
        """
        if (key in pressed_keys):
            keyboard.release(key.value)

    @staticmethod
    def releaseAll():
        """
        releases all currently pressed keys
        """
        for key in pressed_keys():
            Actions.liftKey(key)

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

    @staticmethod
    def press_multiple(keys, duration=0.1):
        """
        Presses multiple keys simultaneously for the specified duration.

        :param keys: List of Keys to press simultaneously.
        :param duration: Time in seconds to hold the keys.
        """
        # Press each key in the list
        for key in keys:
            keyboard.press(key.value)
            # Print which key is being pressed
            print(f"Pressing {key.name}")

        # Hold the keys for the specified duration
        time.sleep(duration)

        # Release each key
        for key in keys:
            keyboard.release(key.value)

    @staticmethod
    def wall_climb(direction, duration=0.1):
        """
        Wall climbs up or down

        :param duration: Time in seconds to hold the keys.
        :param direction: Direction to wall climb, must be up or down (may change later)
        """
        Actions.press_multiple([Keys.GRAB, direction], duration)
