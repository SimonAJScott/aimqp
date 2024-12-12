from keys_enum import Keys
# example [LR, 1.3, 10%]


class Data:
    def __init__(self):
        self.keys = None
        self.press_duration = -1

    def getKeys(self):
        return self.keys

    def setKeys(self, keys: Keys):
        self.keys = keys

    def getPressDuration(self):
        return self.press_duration

    def setPressDuration(self, duration: float):
        self.press_duration = duration

    def printData(self):
        print("Keys:", self.keys, "Press_duration:",
              self.press_duration)
