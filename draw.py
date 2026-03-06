import cv2 as cv
import numpy as np

# Create a black, blank image for testing
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("BLANK", blank)

# 1. Paint a color on image
# blank[:] = 0, 255, 0 # Paint the Entire image by a certain color (Green)
# blank[200:300, 300:400] = 0, 255, 0 # Paint a certain part of the image by a certain color (Green)
# cv.imshow('COLOURED', blank)

# 2. Draw a Rectangle on the image
# cv.rectangle(blank, (0,0), (100,100), (0,250,0), thickness=2) # Rectangle Border Thickness(2)
# cv.rectangle(blank, (0,0), (100,100), (0,250,0), thickness=cv.FILLED) # Rectangle Fill Color
# cv.imshow('RECTANGLE', blank)

# 3. Draw a Circle on the image
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
# cv.imshow('CIRCLE', blank)

# 4. Draw a Line on the image
# cv.line(blank, (100,250), (300, 400), (255, 255, 255), thickness=3)
# cv.imshow("LINE", blank)

# 5. Write a text on the image
# cv.putText(blank, "HELLO ALL", (0, 200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.imshow("TEXT", blank)

cv.waitKey(0)
