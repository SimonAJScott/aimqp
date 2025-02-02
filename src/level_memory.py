import pickle
from data import Data
import random
from keys_enum import Keys
import itertools
from percent_data import PercentData
from input import maxDuration


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
        temp.setPressDuration(round(random.uniform(0, maxDuration), 1))
        return temp

    def update(self, where: int, percentData: PercentData):
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

    def loadData(self, title):
        # Set the filename based on the title
        filename = f"{title}_levelmemorydata.pkl"

        # Load the dictionary from the file
        try:
            with open(filename, "rb") as file:
                # Update self.allData with loaded data
                self.level_data = pickle.load(file)
            print("Level Memory data loaded successfully.")
        except FileNotFoundError:
            print("No file found, created new level-memory dataset")
            return

    def saveData(self, title):
        filename = f"{title}_levelmemorydata.pkl"
        with open(filename, "wb") as file:
            pickle.dump(self.level_data, file)
        print("Saved data:", filename)
