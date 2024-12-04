import pygetwindow as gw
import time
from input import Actions
from level_memory import LevelMemory
from percent_data import PercentData



def main():
    print("This is going to be an interesting project")
    game = "celeste"
    window = gw.getWindowsWithTitle(game)[0]  # find game window
    window.restore()  # open window if minimized
    window.activate()  # put window on top
    time.sleep(2)  # wait a second for game to appear
    algorithmV1(5,20)
    


def algorithmV1(num_generations, num_inputs):
        percentData = PercentData(100) #100 inputs
        print("created percent data")
        currentLevelMemory = LevelMemory(num_inputs)
        for i in range(num_generations):
            print("new generation")
            levelMemoryList = currentLevelMemory.getLevelData()
            print("created current memory")
            for i in range(0,len(levelMemoryList)):
                print("pressing 2 inputs")
                Actions.pressMultiple(levelMemoryList[i])
                #need to add stop when you die and cut off array to recreate
            print("updating memory")
            #LevelMemory.update(currentLevelMemory)


if __name__ == "__main__":
    main()
