from data import Data
from pynput.keyboard import Controller
import time
import random
from keys_enum import Keys

keyboard = Controller()
maxDuration = 1


class Actions:
    """
    A class to input in-game actions. (can add more later)
    """

    def press(self, key, duration):
        """
        presses said button for a certain duration, then lifts

        :param key: must input key enum to work
        :param duration: Time in seconds to hold down button
        """
        keyboard.press(key.value)
        time.sleep(duration)
        keyboard.release(key.value)

    def randomButtons(self, duration=1, wait=0.2):
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

    def pressMultiple(self, data: Data, event):
        """
        Presses multiple buttons for a certain duration, then lifts them.
        """
        if event.is_set():
            event.clear()
            # time.sleep(0.5)  # to try and not trigger cv2 twice
            return 1
        data.printData()
        keys = data.getKeys()
        # Press all keys
        for key in keys:
            keyboard.press(key.value)

        time.sleep(data.getPressDuration())
        # Release all keys
        for key in keys:
            keyboard.release(key.value)
        return 0
