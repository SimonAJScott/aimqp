# Import necessary modules and classes
# Data class to store information related to key presses and durations
from data import Data
import itertools  # To create combinations of keys
from keys_enum import Keys  # Enum class that defines all the available keys
import pickle  # For serializing and deserializing data to and from files
from input import maxDuration  # Maximum duration for a key press


class PercentData:
    """
    Class to handle the generation, updating, saving, and loading of key press percentages.
    The percentages are associated with key combinations and press durations.
    """

    def __init__(self):
        """
        Initializes the PercentData object by generating the initial data.
        """
        self.allData = self.generateInitialData(
        )  # Calls the function to generate initial data

    def generateInitialData(self):
        """
        Generates initial data by creating combinations of keys and assigning percentages to each key-press duration pair.
        Each key combination is associated with a press duration (0-1 second with 0.1-second intervals).
        The percentage is evenly distributed across all combinations.
        """
        # Generate all combinations of keys (2 keys pressed at a time)
        combinations = list(itertools.combinations(list(Keys), 2))

        # Initialize an empty dictionary to store the generated data
        allData = {}

        # Iterate through each combination of keys and press durations
        for keys in combinations:
            # Loop through press durations from 0 to maxDuration in 0.1 increments
            for i in range(maxDuration * 10 + 1):
                # Calculate the initial percentage for each combination and press duration
                tempPercent = 1 / (len(list(combinations))
                                   * (maxDuration * 10))
                # Calculate the press duration in seconds
                tempPressDuration = i / 10
                # Create a key for the combination of keys and press duration
                key = (keys, tempPressDuration)
                # Assign the calculated percentage to the key
                allData[key] = tempPercent

        return allData  # Return the generated dictionary containing key-press duration combinations and their percentages

    def getAllData(self):
        """
        Returns the dictionary containing all the data (key combinations and their corresponding percentages).
        """
        return self.allData

    def saveData(self, title):
        """
        Saves the current data to a file with the given title.
        The data is serialized using pickle.

        :param title: The title to use for the filename.
        """
        filename = f"{title}_percentdata.pkl"  # Construct the filename based on the title

        # Open the file in write-binary mode and serialize the data into the file
        with open(filename, "wb") as file:
            pickle.dump(self.allData, file)
        # Print a message confirming that data was saved
        print("Saved data:", filename)

    def updateData(self, data: list[Data], failed):
        """
        Updates the percentages of the key combinations based on the success or failure of the actions.
        If the action fails, the percentage is reduced by 10%; if successful, it's increased by 1%.

        :param data: A list of Data objects, each containing key combinations and press durations.
        :param failed: A boolean indicating whether the action failed (True) or succeeded (False).
        """
        # Loop through each Data object in the provided list
        for tempData in data:
            # Get the key (key combination and duration)
            key = (tempData.getKeys(), tempData.getPressDuration())
            # Get the current percentage for the key
            currentPercent = self.allData[key]

            # Update the percentage based on whether the action failed or succeeded
            if failed:
                self.allData[key] = currentPercent - \
                    currentPercent * 0.1  # Decrease by 10% if failed
            else:
                # Increase by 1% if successful
                self.allData[key] = currentPercent + currentPercent * 0.01

            # Normalize the percentages to ensure they sum to 1
            # Calculate the total percentage
            total = sum(self.allData.values())
            if total != 1:
                # If the total is not 1, normalize all percentages so they sum to 1
                for key in self.allData:
                    self.allData[key] = self.allData[key] / total

        return len(data)  # Return the number of Data objects processed

    def loadData(self, title):
        """
        Loads previously saved data from a file with the given title.
        The data is deserialized using pickle.

        :param title: The title used to construct the filename of the saved data.
        """
        # Construct the filename based on the title
        filename = f"{title}_percentdata.pkl"

        try:
            # Try to open the file in read-binary mode and load the data from the file
            with open(filename, "rb") as file:
                # Load the data into the allData attribute
                self.allData = pickle.load(file)
            # Print a message confirming data was loaded
            print("Percent data loaded successfully.")
        except FileNotFoundError:
            # If the file doesn't exist, print an error message
            print("No file found, created new percent dataset")
            return
