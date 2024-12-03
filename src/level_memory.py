import data
import input
import random
from input import Keys
import itertools


class LevelMemory:
    def __init__(self, num_inputs: int):
        self.level_data = None
        self.generateRandom(num_inputs)

    def getLevelData(self):
        return self.level_data

    def generateRandom(self, num_inputs):
        randomArray = []
        for i in range(num_inputs):
            randomArray.insert(self.generateInitialRandomData)
        self.level_data = randomArray
    
    def generateInitialRandomData(self):
        # to the nearest tenth from 0-5 seconds. we can change this
        temp = data.Data()
        temp.setKey(random.choice(list(input)))
        temp.setPressDuration(round(random.uniform(0, 5), 1))
        return temp

    def update(self, failedList, failedData: data.Data): # need to update for percentages
        updatedArray = []
        whenBroke = -1
        for i in range(0, len(failedList)):
            updatedArray[i] = failedList[i]
            if (failedList[i] == failedData):
                whenBroke = i-1
                break

        for i in range(whenBroke, len(failedList)):
            if (i == whenBroke+1):
                updatedArray[i] = self.generateRandomData(failedData)
            updatedArray[i] = self.generateRandomData()
        self.level_data = updatedArray

class PercentData:
    def __init__(self, num_inputs:int):
        self.allData = generateInitialData(num_inputs)

    def generateInitialData(self, num_inputs:int):
        combinations = list(itertools.combinations(list(Keys), 2)) #we assume combinations of 2
        allData = []
        for num in range(num_inputs):
            for ele in combinations:
                for i in range(51):
                    temp = data.Data(len(list(Keys))*50)
                    temp.setKeys(ele)
                    temp.setPressDuration(i/10)
            allData.append