import data
import input
import random


class LevelMemory:
    def __init__(self, num_inputs: int):
        self.level_data = None
        self.generateRandom(num_inputs)

    def getLevelData(self):
        return self.level_data

    def generateRandom(self, num_inputs):
        randomArray = []
        for i in range(num_inputs):
            randomArray.insert(self.generateRandomData)
        self.level_data = randomArray

    def update(self, failedList, failedData: data.Data):
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

    def generateRandomData(self):
        # to the nearest tenth from 0-5 seconds. we can change this
        temp = data.Data()
        temp.setKey(random.choice(list(input)))
        temp.setPressDuration(round(random.uniform(0, 5), 1))
        temp.setWaitDuration(round(random.uniform(0, 5), 1))
        return temp

    def generateRandomData(self, failedData: data.Data):
        # to the nearest tenth from 0-5 seconds. we can change this
        temp = data.Data()
        temp.setKey(random.choice(list(input)))
        temp.setPressDuration(round(random.uniform(0, 5), 1))
        temp.setWaitDuration(round(random.uniform(0, 5), 1))
        if (temp == failedData):
            self.generateRandomData(failedData)
        else:
            return temp
