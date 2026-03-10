import cv2 as cv

# Image Reading & Displaying
def read_img():

    # Read image from the local path
    img = cv.imread('images/img_1.jpg')

    # Display image using in-built window
    cv.imshow("ARUN", img)

    # Wait until a Keyboard input to complete code execution
    cv.waitKey(0)

# Video Reading & Displaying
def read_vid():

    # Read video from the local path
    cap = cv.VideoCapture('videos/vid_1.mp4')

    # Opens your Web Cam
    # cap = cv.VideoCapture(0)

    while True:

        # Read individual frames from the video
        isTrue, frame = cap.read()

        # Display the frame using in-built window
        cv.imshow('VIDEO', frame)

        # Code will break after 30s delay or if letter 'd' is pressed from the keyboard
        if cv.waitKey(30) & 0xFF == ord('x'):
            break

    # Releasing the video data from the variable 'cap'
    cap.release()

    # Closing all the windows
    cv.destroyAllWindows()

read_img()
# read_vid()