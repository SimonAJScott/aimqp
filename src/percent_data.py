from data import Data
import itertools
from keys_enum import Keys
import pickle


class PercentData:
    def __init__(self):
        self.allData = self.generateInitialData()

    def generateInitialData(self):
        combinations = list(itertools.combinations(
            list(Keys), 2))  # we assume combinations of 2
        allData = {}
        for keys in combinations:
            for i in range(21):  # assuming 0-5, 0.1 increments (seconds)
                tempPercent = 1/(len(list(combinations))*20)
                tempPressDuration = i/10
                key = (keys, tempPressDuration)
                allData[key] = tempPercent
        return allData

    def getAllData(self):
        return self.allData

    def saveData(self, title):
        filename = f"{title}_percentdata.pkl"
        with open(filename, "wb") as file:
            pickle.dump(self.allData, file)

    def updateData(self, data: Data, failed):
        key = (data.getKeys(), data.getPressDuration())
        currentPercent = self.allData[key]
        n = len(self.allData) - 1
        if failed:
            self.allData[key] = currentPercent - currentPercent*.1

        else:
            self.allData[key] = currentPercent + currentPercent*.01

        total = sum(self.allData.values())
        if total != 1:
            for key in self.allData:
                self.allData[key] = self.allData[key] / total

    def load_and_update_data(self, title):
        # Set the filename based on the title
        filename = f"{title}_percentdata.pkl"

        # Load the dictionary from the file
        try:
            with open(filename, "rb") as file:
                # Update self.allData with loaded data
                self.allData = pickle.load(file)
            print("Data loaded and updated successfully.")
        except FileNotFoundError:
            print(f"{filename} not found. Make sure the file exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
