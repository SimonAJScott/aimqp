import sys
import pygetwindow as gw
import time
from input import Actions
from level_memory import LevelMemory
from percent_data import PercentData
import multiprocessing
import realTime


# Main function to run the game interaction and data handling
def main():
    print("This is going to be an interesting project")

    gamedata = "mario1"  # Game data identifier (for example, "mario1")
    platform = 'Super Mario Bros - Personal - Microsoft​ Edge'  # Title of the game window

    # Get the game window and activate it
    window = gw.getWindowsWithTitle(platform)[0]  # Find the game window
    window.restore()  # Restore the window if minimized
    window.activate()  # Bring the window to the front
    time.sleep(2)  # Wait for the game to fully appear on screen

    # Create an event object to synchronize processes
    event = multiprocessing.Event()

    # Run the main algorithm while monitoring for death state
    algorithmV1(100, 2000, 4, 8, event, gamedata)


# Function to detect if the player dies in the game
def startDeathDetection(event):
    detector = realTime.objectDetection()  # Instantiate object detection class
    detector.find_failstate()  # Check for fail state (death)
    print("Death detection completed.")
    event.set()  # Notify the main process that death has been detected


# Main algorithm function to simulate game actions and update strategy
def algorithmV1(num_generations: int, num_inputs: int, secondsCut: float, waitBetweenGenerations: int, event, game):
    actions = Actions()  # Initialize actions for pressing keys
    percentData = PercentData()  # Initialize percent data to track performance
    percentData.loadData(game)  # Load data specific to the game

    currentLevelMemory = LevelMemory(num_inputs)  # Initialize level memory
    print(num_inputs)  # Print number of inputs for debugging
    currentLevelMemory.loadData(game)  # Load level memory data

    # Loop through generations of gameplay strategy updates
    for i in range(num_generations):
        print(
            f"----------------------- Generation {i + 1} ---------------------")

        levelMemoryList = currentLevelMemory.getLevelData()  # Get current level data

        # Start a new process for death detection
        death_detection_process = multiprocessing.Process(
            target=startDeathDetection, args=(event,))
        death_detection_process.start()
        # Allow time for the death detection process to initialize
        time.sleep(2)

        # Iterate through the level memory list and simulate actions
        for j in range(0, len(levelMemoryList)):
            actionsCut = []  # List to hold actions to be cut off

            # Check if the action is successful (i.e., the character survives)
            if Actions.pressMultiple(actions, levelMemoryList[j], event) == 1:
                secondsPassed = 0
                for k in range(j, 0, -1):
                    # Track the press duration
                    secondsPassed += levelMemoryList[k].getPressDuration()

                    if secondsPassed < secondsCut:  # Cut actions if needed
                        # Add action to cut list
                        actionsCut.append(levelMemoryList[k])

                # Update data based on the actions cut off
                numCut = percentData.updateData(actionsCut, True)

                print(f"NUMBER OF ITEMS BEING CUT: {numCut + 2}")
                # Update the level memory
                currentLevelMemory.update(j - numCut - 2, percentData)
                break  # Stop further action if successful

            # Add to actions if not cut off
            actionsCut.append(levelMemoryList[j])
            # Update the data with new actions
            percentData.updateData(actionsCut, False)

        # Wait for the death detection process to finish
        print("Waiting for death screen to finish...")
        time.sleep(waitBetweenGenerations)

    # Save updated data after completing all generations
    percentData.saveData(game)
    currentLevelMemory.saveData(game)
    sys.exit()  # Exit the program when done


if __name__ == "__main__":
    main()  # Start the main function
