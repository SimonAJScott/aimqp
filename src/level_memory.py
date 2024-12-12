from data import Data
import random
from keys_enum import Keys
import itertools


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
        temp.setPressDuration(round(random.uniform(0, 5), 1))
        return temp

    # def update(self, failedList, failedData: Data): # need to update for percentages
    #     updatedArray = []
    #     whenBroke = -1
    #     for i in range(0, len(failedList)):
    #         updatedArray[i] = failedList[i]
    #         if (failedList[i] == failedData):
    #             whenBroke = i-1
    #             break

    #     for i in range(whenBroke, len(failedList)):
    #         if (i == whenBroke+1):
    #             updatedArray[i] = self.generateRandomData(failedData)
    #         updatedArray[i] = self.generateRandomData()
    #     self.level_data = updatedArray
