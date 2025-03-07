import pickle  # Import pickle module to serialize and deserialize Python objects
# Import the 'Data' class from the 'data' module to store key press data
from data import Data
import random  # Import random module for generating random numbers and choices
from keys_enum import Keys  # Import the 'Keys' enum class to use key actions
import itertools  # Import itertools for generating combinations
# Import the 'PercentData' class to handle percentage data
from percent_data import PercentData
from input import maxDuration  # Import 'maxDuration' to limit the press duration


class LevelMemory:
    """
    A class to manage and store the level data in memory, including generating random data, 
    updating data, and loading/saving data from/to a file.
    """

    def __init__(self, num_inputs: int):
        """
        Initializes the LevelMemory instance by setting the 'level_data' to None and generating
        random level data based on the number of inputs provided.

        :param num_inputs: Number of random inputs to generate for the level data
        """
        self.level_data = None  # Level data will store a list of 'Data' objects
        # Generate random level data based on the number of inputs
        self.generateRandom(num_inputs)

    def getLevelData(self):
        """
        Retrieve the current level data.

        :return: The level data stored as a list of 'Data' objects
        """
        return self.level_data

    def printLevelData(self):
        """
        Print the current level data by iterating through the list of 'Data' objects.
        """
        for data in self.level_data:
            data.printData()  # Print each Data object's information

    def generateRandom(self, num_inputs):
        """
        Generate random level data with the specified number of inputs. 
        Each data entry is created using 'generateInitialRandomData'.

        :param num_inputs: Number of random data entries to generate
        """
        randomArray = []  # Create an empty list to store random data entries
        for i in range(num_inputs):
            # Generate initial random data and insert it
            randomArray.insert(i, self.generateInitialRandomData())
        # Store the generated random data in the 'level_data' attribute
        self.level_data = randomArray

    def generateInitialRandomData(self):
        """
        Generate initial random data for the level. The press duration is randomized between 0 and 'maxDuration',
        and the keys are randomly selected from combinations of the 'Keys' enum.

        :return: A Data object with random keys and press duration
        """
        temp = Data()  # Create a new Data object to store the random key press data
        # Generate all possible 2-key combinations
        combinationsList = list(itertools.combinations(list(Keys), 2))
        # Set random 2-key combination
        temp.setKeys(random.choice(combinationsList))
        # Set random press duration rounded to the nearest tenth
        temp.setPressDuration(round(random.uniform(0, maxDuration), 1))
        return temp

    def update(self, where: int, percentData: PercentData):
        """
        Update the level data starting from the specified index 'where'. The keys and press duration 
        are updated based on the weighted random choices provided by the 'PercentData'.

        :param where: The index to start updating from
        :param percentData: The 'PercentData' object containing options and weights for the updates
        """
        self.level_data[
            # Access the level data at the specified index (but doesn't modify it yet)
            where]
        # Extract the options (keys and durations) from 'percentData'
        options = list(percentData.allData.keys())
        # Extract the weights for the options
        weights = list(percentData.allData.values())

        # Update the level data from the specified index to the end of the list
        for i in range(where, len(self.level_data)):
            temp = Data()  # Create a new Data object for each level entry
            # Randomly select keys and duration based on weights
            keys = random.choices(options, weights=weights, k=1)[0]
            temp.setKeys(keys[0])  # Set the selected key
            # Set the corresponding press duration
            temp.setPressDuration(keys[1])
            # Update the level data at the current index
            self.level_data[i] = temp

    def loadData(self, title):
        """
        Load the level data from a file based on the provided title. The file is expected to be in pickle format.

        :param title: The title used to generate the filename for loading the data
        """
        filename = f"{title}_levelmemorydata.pkl"  # Generate the filename based on the title

        try:
            # Attempt to open the file and load the data
            with open(filename, "rb") as file:
                # Load the level data from the file
                self.level_data = pickle.load(file)
            print("Level Memory data loaded successfully.")
        except FileNotFoundError:
            # Handle case where the file doesn't exist
            print("No file found, created new level-memory dataset")

    def saveData(self, title):
        """
        Save the current level data to a file based on the provided title. The data is serialized using pickle.

        :param title: The title used to generate the filename for saving the data
        """
        filename = f"{title}_levelmemorydata.pkl"  # Generate the filename based on the title
        # Open the file in write-binary mode and save the level data
        with open(filename, "wb") as file:
            # Serialize and write the level data to the file
            pickle.dump(self.level_data, file)
        print("Saved data:", filename)  # Print confirmation of the saved data
