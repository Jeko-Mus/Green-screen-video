import cv2
import numpy as np
import matplotlib.pyplot as plt

# import image and video to be used
video = cv2.VideoCapture('img/green_video.mp4')
image = cv2.imread('img/beach.jpg')

while True:
    ret, frame = video.read()
    # resize to same sizes
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))

    #hsv colour map so we can extract ranges for colour green
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #for green colours the upper and lower bounds on hsv colour map are
    lower_bound = (38,40, 20)
    upper_bound = (85, 255,255)

    # mask to green colour range
    mask = cv2.inRange(hsv_image, lower_bound,upper_bound)
    final_image = cv2.bitwise_and(frame,frame, mask=mask)

    # remove/subtract green screen part to remain with just the image
    f = frame - final_image
    # replace blank/black screen(0,0,0) with our original image background
    f = np.where(f == 0, image, f)
    
    cv2.imshow('my video', frame)
    cv2.imshow('mask', f)

    if cv2.waitKey(5) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()