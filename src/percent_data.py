import data
import itertools
from keys_enum import Keys


class PercentData:
    def __init__(self):
        self.allData = self.generateInitialData()

    def generateInitialData(self):
        combinations = list(itertools.combinations(
            list(Keys), 2))  # we assume combinations of 2
        allData = {}
        for keys in combinations:
            for i in range(51):  # assuming 0-5, 0.1 increments (seconds)
                tempPercent = 1/(len(list(combinations))*50)
                tempPressDuration = i/10
                key = (keys, tempPressDuration)
                allData[key] = tempPercent
        return allData

    def getAllData(self):
        return self.allData
