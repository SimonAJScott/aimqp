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


class Actions:
    """
    A class to input in-game actions. (can add more later)

    Methods:
    -------
    random():
        Presses random buttons (did not implement multiple buttons, can change later)
    press_multiple():
        Presses multiple keys simultaneously for the specified duration.
    dash():
        Have multiple dash functions
        right
        left
        up
        down
        right+up
        right+down
        left+up
        left+down
    """
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
            key_to_press.press()  # Press the randomly selected key
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
    def dash_right(duration=0.1):
        """
        Inputs dash+right

        :param duration: Time in seconds to hold the keys.
        """
        Actions.press_multiple([Keys.DASH, Keys.RIGHT], duration)

    @staticmethod
    def dash_up(duration=0.1):
        """
        Inputs dash+up

        :param duration: Time in seconds to hold the keys.
        """
        Actions.press_multiple([Keys.DASH, Keys.UP], duration)

    @staticmethod
    def dash_down(duration=0.1):
        """
        Inputs dash+down

        :param duration: Time in seconds to hold the keys.
        """
        Actions.press_multiple([Keys.DASH, Keys.DOWN], duration)

    @staticmethod
    def dash_left(duration=0.1):
        """
        Inputs dash+left

        :param duration: Time in seconds to hold the keys.
        """
        Actions.press_multiple([Keys.DASH, Keys.LEFT], duration)

    @staticmethod
    def dash_right_up(duration=0.1):
        """
        Inputs dash+right+up

        :param duration: Time in seconds to hold the keys.
        """
        Actions.press_multiple([Keys.DASH, Keys.RIGHT, Keys.UP], duration)

    @staticmethod
    def dash_right_down(duration=0.1):
        """
        Inputs dash+right+down

        :param duration: Time in seconds to hold the keys.
        """
        Actions.press_multiple([Keys.DASH, Keys.RIGHT, Keys.DOWN], duration)

    @staticmethod
    def dash_left_down(duration=0.1):
        """
        Inputs dash+left+down

        :param duration: Time in seconds to hold the keys.
        """
        Actions.press_multiple([Keys.DASH, Keys.LEFT, Keys.DOWN], duration)

    @staticmethod
    def dash_left_up(duration=0.1):
        """
        Inputs dash+left+up

        :param duration: Time in seconds to hold the keys.
        """
        Actions.press_multiple([Keys.DASH, Keys.LEFT, Keys.UP], duration)

    @staticmethod
    def wall_climb(direction, duration=0.1):
        """
        Wall climbs up

        :param duration: Time in seconds to hold the keys.
        :param direction: Direction to wall climb, must be up or down (may change later)
        """
        Actions.press_multiple([Keys.GRAB, direction], duration)
