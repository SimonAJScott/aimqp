import pygetwindow as gw
import time
from keys import Keys
import random
if __name__ == "__main__":
    print("This is going to be an interesting project")
    game = "celeste"
    window = gw.getWindowsWithTitle(game)[0]  # find game window
    window.restore()  # open window if minimized
    window.activate()  # put window on top
    time.sleep(2)  # wait a second for game to appear
    Keys.JUMP.press()
    start_time = time.time()  # Record the start time
    end_time = start_time + 5  # Run for 5 seconds

    while time.time() < end_time:
        key_to_press = random.choice(list(Keys))  # Randomly choose a key
        # Print which key is being pressed
        print(f"Pressing {key_to_press.name}")
        # key_to_press.press()  # Press the randomly selected key
        time.sleep(0.5)  # Sleep for half a second between presses
