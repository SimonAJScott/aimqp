from keys_enum import Keys  # Import the 'Keys' enum class from the 'keys_enum' module


class Data:
    """
    A class to store and manage information related to key presses and their durations.
    """

    def __init__(self):
        """
        Initialize an instance with 'keys' set to None and 'press_duration' set to -1.
        'keys' will hold the keys pressed (could be an instance of the 'Keys' enum).
        'press_duration' will store the duration of the key press (initially set to -1).
        """
        self.keys = None  # 'keys' attribute to store the pressed keys
        self.press_duration = -1  # 'press_duration' to store how long a key was pressed

    def getKeys(self):
        """
        Retrieve the current keys pressed.

        :return: The keys pressed (an instance of the 'Keys' enum or None if not set).
        """
        return self.keys

    def setKeys(self, keys: Keys):
        """
        Set the keys pressed, expecting an instance of the 'Keys' enum.

        :param keys: The keys pressed, passed as an instance of 'Keys'.
        """
        self.keys = keys

    def getPressDuration(self):
        """
        Retrieve the duration for which the keys were pressed.

        :return: The duration the keys were pressed (a float).
        """
        return self.press_duration

    def setPressDuration(self, duration: float):
        """
        Set the press duration, expecting a float representing the duration in seconds.

        :param duration: The duration in seconds for how long the key was pressed.
        """
        self.press_duration = duration

    def printData(self):
        """
        Print the current state of the 'keys' and 'press_duration' attributes.
        This can be used to check the current data stored in the instance.
        """
        print("Keys:", self.keys, "Press_duration:", self.press_duration)
