import cv2 as cv

# Rescale the given Frame (Images, Videos & Live Video)
def rescale_frame(frame, scale = 0.75):

    # Rescaling the Width of the original frame
    width = int(frame.shape[1] * scale)

    # Rescaling the Height of the original frame
    height = int(frame.shape[0] * scale)

    # Keeping the Rescaled dimension in a Tuple
    dimensions = (width, height)

    # Rescaling the frame using in-built library & returning it to th
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Change the resolution of the Video (Only Live Videos)
def change_res(cap, width, height):

    cap.set(3, width)
    cap.set(4, height)

# Image Reading & Displaying
def read_img():

    # Read image from the local path
    img = cv.imread('images/img_1.jpg')

    img_resized = rescale_frame(img)

    # Display image using in-built window
    cv.imshow("IMAGE", img)

    # Display Resized image using in-built window
    cv.imshow("RESIZED IMAGE", img_resized)

    # Wait until a Keyboard input to complete code execution
    cv.waitKey(0)


# Video Reading & Displaying
def read_vid():

    # Read video from the local path
    cap = cv.VideoCapture('videos/vid_1.mp4')

    while True:

        # Read individual frames from the video
        isTrue, frame = cap.read()

        # Resized frame of Original frame
        frame_resized = rescale_frame(frame, scale=0.2)

        # Display the frame using in-built window
        cv.imshow('VIDEO', frame)

        # Display the Resized frame using in-built window
        cv.imshow('RESIZED VIDEO', frame_resized)

        # Code will break after 30s delay or if letter 'd' is pressed from the keyboard
        if cv.waitKey(30) & 0xFF == ord('d'):
            break

    # Releasing the video data from the variable 'cap'
    cap.release()

    # Closing all the windows
    cv.destroyAllWindows()

read_img()
read_vid()
