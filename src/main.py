import pygetwindow as gw
import time
from input import Actions
from level_memory import LevelMemory
from percent_data import PercentData
import multiprocessing
import realTime


# save data based on input (name of game)
def main():
    print("This is going to be an interesting project")
    game = "celeste"
    window = gw.getWindowsWithTitle(game)[0]  # find game window
    window.restore()  # open window if minimized
    window.activate()  # put window on top
    time.sleep(2)  # wait a second for game to appear

    # Create an Event object for synchronization
    event = multiprocessing.Event()

    # Run the algorithm while death detection is ongoing
    algorithmV1(10, 100, event)


def startDeathDetection(event):
    detector = realTime.objectDetection()
    detector.find_failstate()  # To detect fail state
    # Once the fail state is detected, set the event
    print("Death detection completed.")
    event.set()


def algorithmV1(num_generations, num_inputs, event):
    actions = Actions()
    percentData = PercentData()
    print("created percent data")
    currentLevelMemory = LevelMemory(num_inputs)
    currentLevelMemory.printLevelData()
    for i in range(num_generations):
        print("-----------------------generation ",
              i+1, " ---------------------")
        levelMemoryList = currentLevelMemory.getLevelData()
        print("created current memory")
        # Start a new process for death detection at the start of each generation
        death_detection_process = multiprocessing.Process(
            target=startDeathDetection, args=(event,))
        death_detection_process.start()
        time.sleep(2)
        for j in range(0, len(levelMemoryList)):
            # need to add stop when you die and cut off array to recreate
            if (Actions.pressMultiple(actions, levelMemoryList[j], event) == 1):
                percentData.updateData(levelMemoryList[j], True)
                currentLevelMemory.update(j, percentData)
                break
            percentData.updateData(levelMemoryList[j], False)
    exit(1)


if __name__ == "__main__":
    main()
