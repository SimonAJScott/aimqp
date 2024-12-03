import cv2 as cv
import numpy as np
import os
from time import time
from windowCapture import WindowCapture
from vision import Vision

#os.chdir(os.path.dirname(os.path.abspath(__file__)))

class objectDetection:
   
    #Properties
    def __init__(self):
        wincap = None
        vision_detect = None
        screenshot = None
        points = None
        loop_time = time()

    def find_failstate(self):
        # initialize the WindowCapture class
        self.wincap = WindowCapture('Celeste')
        # initialize the Vision class
        self.vision_detect = Vision('anglesbig.jpg')

        self.loop_time = time()
        testNum = 0
        while(True):

            # get an updated image of the game
            self.screenshot = self.wincap.get_screenshot()

            # display the processed image
            if self.screenshot is not None:
                self.points = self.vision_detect.find(self.screenshot, 0.46, 'rectangles')
            if self.points:
                #cv.destroyAllWindows()
                #break
                print('lmao died ->',testNum)
                testNum = testNum + 1
            #points = vision_example.find(screenshot, 0.7, 'points')

            # debug the loop rate
            #print('FPS {}'.format(1 / (time() - self.loop_time)))
            self.loop_time = time()

            # press 'p' with the output window focused to exit.
            # waits 1 ms every loop to process key presses
            
            if cv.waitKey(1) == ord('p'):
                cv.destroyAllWindows()
                break

        print('Done.')

detector = objectDetection()
detector.find_failstate()  # To detect fail state