import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

cv.imshow("BLANK", blank)

blank[:] = 0, 255, 0

cv.imshow('GREEN', blank)

cv.waitKey(0)
