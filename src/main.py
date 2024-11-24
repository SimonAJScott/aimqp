import pygetwindow as gw
import time
from input import Actions as action
from input import Keys


def main():
    print("This is going to be an interesting project")
    game = "celeste"
    window = gw.getWindowsWithTitle(game)[0]  # find game window
    window.restore()  # open window if minimized
    window.activate()  # put window on top
    time.sleep(2)  # wait a second for game to appear


if __name__ == "__main__":
    main()
