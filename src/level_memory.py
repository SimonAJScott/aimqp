from data import Data
import random
from keys_enum import Keys
import itertools
from percent_data import PercentData


class LevelMemory:
    def __init__(self, num_inputs: int):
        self.level_data = None
        self.generateRandom(num_inputs)

    def getLevelData(self):
        return self.level_data

    def printLevelData(self):
        for data in self.level_data:
            data.printData()

    def generateRandom(self, num_inputs):
        randomArray = []
        for i in range(num_inputs):
            randomArray.insert(i, self.generateInitialRandomData())
        self.level_data = randomArray

    def generateInitialRandomData(self):
        # to the nearest tenth from 0-5 seconds. we can change this
        temp = Data()
        combinationsList = list(itertools.combinations(list(Keys), 2))
        temp.setKeys(random.choice(combinationsList))
        temp.setPressDuration(round(random.uniform(0, 2), 1))
        return temp

    def update(self, where: int, percentData: PercentData):
        where = where - 3
        self.level_data[where]
        options = list(percentData.allData.keys())
        weights = list(percentData.allData.values())
        for i in range(where, len(self.level_data)):
            temp = Data()
            keys = random.choices(
                options, weights=weights, k=1)[0]
            temp.setKeys(keys[0])
            temp.setPressDuration(keys[1])
            self.level_data[i] = temp
