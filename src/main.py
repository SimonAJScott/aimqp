import pygetwindow as gw
import time
from input import Actions
from level_memory import LevelMemory
from percent_data import PercentData


# save data based on input (name of game)
def main():
    print("This is going to be an interesting project")
    game = "celeste"
    window = gw.getWindowsWithTitle(game)[0]  # find game window
    window.restore()  # open window if minimized
    window.activate()  # put window on top
    time.sleep(2)  # wait a second for game to appear
    algorithmV1(5, 20)


def algorithmV1(num_generations, num_inputs):
    actions = Actions()
    percentData = PercentData()
    print("created percent data")
    currentLevelMemory = LevelMemory(num_inputs)
    currentLevelMemory.printLevelData()
    for i in range(num_generations):
        print("new generation")
        levelMemoryList = currentLevelMemory.getLevelData()
        print("created current memory")
        for data in range(0, len(levelMemoryList)):
            print("pressing 2 inputs")
            Actions.pressMultiple(actions, levelMemoryList[data])
            # need to add stop when you die and cut off array to recreate
        print("updating memory")
        # LevelMemory.update(currentLevelMemory)


if __name__ == "__main__":
    main()
