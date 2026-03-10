import cv2 as cv

# Read image from the local path
img = cv.imread('images/img_1.jpg')
cv.imshow("ORIGINAL", img)

# 1. Convert the Colour image into Gray Scale image
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY SCALE", gray)

# 2. Apply Blur on original image using Gaussian Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("BLUR", blur)

# 3. Edge Cascade using Canny Edge function
canny = cv.Canny(img, 125, 175)
cv.imshow("CANNY EDGE", canny)

# 4. Dilating the Image using Canny Edge image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("DILATED", dilated)

# 5. Eroding the Image using Dilated image
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("ERODED", eroded)

# 6. Resizing the Original image into a desired sizee
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("RESIZED", resized)

# 7. Cropping the image based on Co-Ordinates
cropped = img[50:200, 200:400]
cv.imshow("CROPPED", cropped)

# Wait until a Keyboard input to complete code execution
cv.waitKey(0)