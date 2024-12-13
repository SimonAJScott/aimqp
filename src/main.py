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
    algorithmV1(2, 100, 2.5, event, game)


def startDeathDetection(event):
    detector = realTime.objectDetection()
    detector.find_failstate()  # To detect fail state
    # Once the fail state is detected, set the event
    print("Death detection completed.")
    event.set()


def algorithmV1(num_generations: int, num_inputs: int, secondsCut: float, event, game):
    actions = Actions()
    percentData = PercentData()
    percentData.loadData(game)
    currentLevelMemory = LevelMemory(num_inputs)
    currentLevelMemory.loadData(game)
    for i in range(num_generations):
        print("-----------------------generation ",
              i+1, " ---------------------")
        levelMemoryList = currentLevelMemory.getLevelData()
        # Start a new process for death detection at the start of each generation
        death_detection_process = multiprocessing.Process(
            target=startDeathDetection, args=(event,))
        death_detection_process.start()
        time.sleep(2)
        for j in range(0, len(levelMemoryList)):
            actionsCut = []
            # need to add stop when you die and cut off array to recreate
            if (Actions.pressMultiple(actions, levelMemoryList[j], event) == 1):
                secondsPassed = 0
                for k in range(j, 0, -1):
                    secondsPassed = secondsPassed + \
                        levelMemoryList[k].getPressDuration()
                    if secondsPassed < secondsCut:
                        actionsCut.append(levelMemoryList[k])
                numCut = percentData.updateData(actionsCut, True)

                # calculate which actions to update in helper
                print("NUMBER OF ITEMS BEING CUT:", numCut)
                currentLevelMemory.update(j-numCut-2, percentData)
                break
            actionsCut.append(levelMemoryList[j])
            percentData.updateData(actionsCut, False)
    percentData.saveData(game)  # change later based on game
    currentLevelMemory.saveData(game)
    exit(1)


if __name__ == "__main__":
    main()
