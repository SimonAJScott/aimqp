import cv2 as cv
import numpy as np
import os
from time import time
from windowCapture import WindowCapture
from vision import Vision


class objectDetection:

    # properties
    def __init__(self):
        wincap = None
        vision_detect = None
        screenshot = None
        points = None
        loop_time = time()

    def find_failstate(self):
        # this works assuming the game being run has a death screen which can be added
        # initialize the WindowCapture class
        # write the exact name of the program file being run, if it is not exact it will not work. Certain games also have potential conflicts when recorded which may cause issues.
        self.wincap = WindowCapture(
            'Super Mario Bros - Personal - Microsoft​ Edge')
        # initialize the Vision class
        # add the image of the death screen below
        self.vision_detect = Vision('anglestest.jpg')

        self.loop_time = time()
        testNum = 0
        while (True):

            # get an updated image of the game
            self.screenshot = self.wincap.get_screenshot()

            # display the processed image
            if self.screenshot is not None:
                self.points = self.vision_detect.find(
                    self.screenshot, 0.8, 'rectangles')
                # change the number in order to change the accuracy of the threshold. example self.points = self.vision_detect.find(self.screenshot, 0.67, 'rectangles')
            if self.points:
                # prints a statement confirming a failure
                print('lmao died ->', testNum)
                testNum = testNum + 1
            # debug the loop rate
            # print('FPS {}'.format(1 / (time() - self.loop_time)))
            self.loop_time = time()

            # press 'p' with the output window focused to exit.
            # waits 1 ms every loop to process key presses

            if cv.waitKey(1) == ord('p'):
                cv.destroyAllWindows()
                break

        print('Done.')


detector = objectDetection()
detector.find_failstate()  # To detect fail state
