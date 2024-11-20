import cv2 as cv
import numpy as np


#loading in image
celeste_img = cv.imread('full image5.jpg', cv.IMREAD_UNCHANGED)
madeline_img = cv.imread('zoomed in.jpg', cv.IMREAD_UNCHANGED)


#getting result
result = cv.matchTemplate(celeste_img, madeline_img, cv.TM_CCOEFF_NORMED)

#get best match position(coordinates)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
print('best match top left position: %s' % str(max_loc))
print('best match confidence: %s' %max_val)

#threshold for accuracy in finding match
threshold = 0.5
if max_val >= threshold:
    print('found object')

    #get object dimensions
    madeline_w = madeline_img.shape[1]
    madeline_h = madeline_img.shape[0]

    #find image top left and bottom right
    top_left = max_loc
    bottom_right = (top_left[0]+ madeline_w, top_left[1] + madeline_h)
    
    #outline image
    cv.rectangle(celeste_img, top_left, bottom_right, color=(0,0,255), thickness=3, lineType=cv.LINE_4)
    #displaying result
    cv.imshow('Result', celeste_img)

    cv.waitKey() #pauses script so you can see result
else:
    print('did not find object')