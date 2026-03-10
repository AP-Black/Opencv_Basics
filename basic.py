import cv2 as cv

# Read image from the local path
img = cv.imread('images/img_1.jpg')
cv.imshow("ORIGINAL", img)

# 1. Convert the Colour image into Gray Scale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY SCALE", gray)

# 2. Apply Blur on original image using Gaussian Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("BLUR", blur)

# # 3. Edge Cascade using Canny Edge function
canny_1 = cv.Canny(img, 200, 200) 
cv.imshow("CANNY EDGE-1", canny_1)

canny_2 = cv.Canny(img, 200, 500) 
cv.imshow("CANNY EDGE-2", canny_2)

# # 4. Dilating the Image using Canny Edge image
dilated = cv.dilate(canny_1, (7,7), iterations=1)
cv.imshow("DILATED", dilated)

# # 5. Eroding the Image using Dilated image
eroded = cv.erode(canny_1, (7,7), iterations=1)
cv.imshow("ERODED", eroded)

# # 6. Resizing the Original image into a desired sizee
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LANCZOS4)
cv.imshow("RESIZED", resized)

# # 7. Cropping the image based on Co-Ordinates
cropped = img[100:200, 50:400] # img[y-axis starting point:y-axis ending point, x-axis starting point:x-axis ending point]
cv.imshow("CROPPED", cropped)

# Wait until a Keyboard input to complete code execution
cv.waitKey(0)