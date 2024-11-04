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
    # randomButtons(3)
    action.dash_left_up()
    action.wall_climb(Keys.UP, 2)


if __name__ == "__main__":
    main()
