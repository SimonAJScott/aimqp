import data
import itertools
from keys_enum import Keys

class PercentData:
    def __init__(self, num_inputs:int):
        self.allData = self.generateInitialData(num_inputs)

    def generateInitialData(self, num_inputs:int):
        combinations = list(itertools.combinations(list(Keys), 2)) #we assume combinations of 2
        allData = []
        for num in range(num_inputs):
            for ele in combinations:
                for i in range(51):
                    temp = data.Data(len(list(Keys))*50)
                    temp.setKeys(ele)
                    temp.setPressDuration(i/10)
            allData.append(temp)
        return allData