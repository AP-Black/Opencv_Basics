# Code Execution=> python .\detect_lines.py .\images\img_blank.jpg  

import cv2 as cv
import numpy as np
import sys
import os
from datetime import datetime

def detect_lines(image_path: str, can_save = False):
    
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    # Load image
    img = cv.imread(image_path)
    if img is None:
        print(f"Error: Could not read image '{image_path}'.")
        sys.exit(1)

    output = img.copy()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # --- Preprocessing ---
    # Blur to reduce noise, then use Canny edge detection
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    edges = cv.Canny(blurred, threshold1=30, threshold2=100)

    # --- Line detection via Probabilistic Hough Transform ---
    lines = cv.HoughLinesP(
        edges,
        rho=1,              # Distance resolution (pixels)
        theta=np.pi / 180,  # Angle resolution (radians)
        threshold=20,       # Min votes to qualify as a line
        minLineLength=15,   # Min length of a line segment (pixels)
        maxLineGap=10       # Max gap between segments to treat as one line
    )

    if lines is None or len(lines) == 0:
        cv.putText(output, "OK", (0, 100), cv.FONT_HERSHEY_TRIPLEX, 4.0, (0,255,0), 2)
         
    else:
        cv.putText(output, "NOK", (0, 100), cv.FONT_HERSHEY_TRIPLEX, 4.0, (0,0,255), 2)
        print(f"Detected {len(lines)} line segment(s):")

        # Draw each detected line on the output image
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(output, (x1, y1), (x2, y2), (0, 255, 255), 2)  # Yellow highlight

    cv.imshow('INPUT', rescale_frame(img, 0.25))
    cv.imshow('OUTPUT', rescale_frame(output, 0.25))
    
    cv.waitKey(0)
    cv.destroyAllWindows()

    if can_save:
        op_img_name = f"img_op_{datetime.now().strftime('%y%m%d%H%M%S')}.jpg"
        op_path = os.path.join(os.path.dirname(image_path), op_img_name)
        cv.imwrite(op_path, output)

# Rescale the given Frame
def rescale_frame(frame, scale = 0.75):

    # Rescaling the Width of the original frame
    width = int(frame.shape[1] * scale)

    # Rescaling the Height of the original frame
    height = int(frame.shape[0] * scale)

    # Keeping the Rescaled dimension in a Tuple
    dimensions = (width, height)

    # Rescaling the frame using in-built library & returning it
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python detect_lines.py <image_path>")
        print("Example: python detect_lines.py photo.jpg")
        sys.exit(1)

    detect_lines(sys.argv[1], False)
