import cv2 as cv
import numpy as np

import cv2 as cv
import numpy as np

# inspired from https: // www.youtube.com/playlist?list = PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI


class Vision:

    # properties
    playerCharacter_img = None
    playerCharacter_w = 0
    playerCharacter_h = 0
    method = None

    # constructor
    def __init__(self, playerCharacter_img_path, method=cv.TM_CCOEFF_NORMED):
        # load the image we're trying to match
        # https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html
        self.playerCharacter_img = cv.imread(
            playerCharacter_img_path, cv.IMREAD_UNCHANGED)

        # Save the dimensions of the playerCharacter image
        self.playerCharacter_w = self.playerCharacter_img.shape[1]
        self.playerCharacter_h = self.playerCharacter_img.shape[0]

        # There are 6 methods to choose from:
        # TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
        self.method = method

    def find(self, fullGame_img, threshold=0.5, debug_mode=None):
        # run the OpenCV algorithm
        result = cv.matchTemplate(
            fullGame_img, self.playerCharacter_img, self.method)

        # Get the all the positions from the match result that exceed our threshold
        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]),
                    self.playerCharacter_w, self.playerCharacter_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(
            rectangles, groupThreshold=1, eps=0.5)
        # print(rectangles)

        points = []
        if len(rectangles):
            # print('Found playerCharacter.')

            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS

            # Loop over all the rectangles
            for (x, y, w, h) in rectangles:

                # Determine the center position
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                # Save the points
                points.append((center_x, center_y))

                if debug_mode == 'rectangles':
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv.rectangle(fullGame_img, top_left, bottom_right, color=line_color,
                                 lineType=line_type, thickness=2)
                elif debug_mode == 'points':
                    # Draw the center point
                    cv.drawMarker(fullGame_img, (center_x, center_y),
                                  color=marker_color, markerType=marker_type,
                                  markerSize=40, thickness=2)

        # if debug_mode:
        #     cv.imshow('Matches', fullGame_img)
        #     # cv.waitKey()
        #     # cv.imwrite('result_click_point.jpg', fullGame_img)

        return points

# MIT License

# Copyright (c) 2023 Ben Johnson

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
