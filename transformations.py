import cv2 as cv
import numpy as np

# Read image from the local path
img = cv.imread('images/img_1.jpg')
cv.imshow("ORIGINAL", img)

# Translate the image by x and y co-ordinates
def translate(img, x, y): # x => Right, -x => Left, y => Down, -y => Up
    transMat = np.float32([[1,0,x],[0,1,y]])
    # Get the Width & Height of the Image
    dimensions = (img.shape[1], img.shape[0])
    # Translate the image by the specific co-ordinates using in-built function
    return cv.warpAffine(img, transMat, dimensions)

# Display the Translated Image
translated = translate(img, 200, 100)
cv.imshow("TRANSLATED", translated)

def rotate(img, angle, rotPoint=None): # angle => Clockwise & -angle => Anti-Clockwise

    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate (img, 45, (100, 100))
cv.imshow("ROTATED", rotated)

flip = cv.flip(img, 0) # -1 => Vertical Flip & 1 => Horizontal Flip
cv.imshow("FLIPPED", flip)

cv.waitKey(0)