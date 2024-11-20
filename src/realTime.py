import cv2 as cv
import numpy as np
import os
from time import time
from windowCapture import WindowCapture
from vision import Vision

#os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Celeste')
# initialize the Vision class
vision_player = Vision('zoomed in right3.jpg') or Vision('zoomed in left3.jpg')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_player.find(screenshot, 0.5, 'rectangles')
    #points = vision_example.find(screenshot, 0.7, 'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    
    if cv.waitKey(1) == ord('p'):
        cv.destroyAllWindows()
        break

print('Done.')

loop_time2 = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_player.find(screenshot, 0.5, 'rectangles')
    #points = vision_example.find(screenshot, 0.7, 'points')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'p' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    
    if cv.waitKey(1) == ord('p'):
        cv.destroyAllWindows()
        break

print('Done.')