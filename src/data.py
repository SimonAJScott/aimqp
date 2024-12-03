from input import Keys
# example [LR, 1.3, 10%]


class Data:
    def __init__(self, num_inputs):
        self.keys = None
        self.press_duration = -1
        self.percentage = 1/num_inputs

    # Define equality comparison
    def __eq__(self, other):
        if not isinstance(other, Data):
            return False
        return (self.keys == other.keys and
                self.press_duration == other.press_duration and
                self.percentage == other.percentage)

    def getKeys(self):
        return self.keys

    def setKeys(self, keys: Keys):
        self.keys = keys

    def getPressDuration(self):
        return self.press_duration

    def setPressDuration(self, duration: int):
        self.press_duration = duration

    def getPercentage(self):
        return self.percentage

    def setPercentage(self, percent: float):
        self.percentage = percent
