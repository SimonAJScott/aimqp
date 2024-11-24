from input import Keys
# example [L,3,10]
# multiprocessing or math (queue?)
# [L,3,10] [J,2,5]


class Data:
    def __init__(self):
        self.key = None
        self.press_duration = -1
        self.wait_duration = -1

    # Define equality comparison
    def __eq__(self, other):
        if not isinstance(other, Data):
            return False
        return (self.key == other.key and
                self.press_duration == other.press_duration and
                self.wait_duration == other.wait_duration)

    def getKey(self):
        return self.key

    def setKey(self, key: Keys):
        self.key = key

    def getPressDuration(self):
        return self.press_duration

    def setPressDuration(self, duration: int):
        self.press_duration = duration

    def getWaitDuration(self):
        return self.wait_duration

    def setWaitDuration(self, wait: int):
        self.wait_duration = wait
