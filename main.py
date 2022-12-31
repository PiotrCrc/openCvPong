import cv2 as cv
import numpy as np
from ponggame import ponggame


if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    first = True
    while(1):
        # Take each frame
        _, frame = cap.read()
        if first:
            new_game = ponggame(frame.shape[0],frame.shape[1])
            first = False
        # Convert BGR to HSV
        new_frame = frame.copy()
        new_frame2 = frame.copy()
        cv.rectangle(new_frame2, (0, 0), (640, 480), (255, 0, 255), -1)
        cv.rectangle(new_frame, (20, 0), (620, 480), (255, 255, 255), -1)
        hsv = cv.cvtColor(new_frame, cv.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower = np.array([0,0,0])
        upper = np.array([255,255,20])
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower, upper)
        cv.imshow('mask', mask)
        mask = cv.bitwise_not(mask)
        # Bitwise-AND mask and original image

        res = cv.bitwise_or(new_frame2, frame, mask = mask)

        new_game.nastpena_klatka()
        new_game.rysuj_pilke(res)

        #cv.imshow('frame',frame)


        cv.imshow('res',res)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break

    cv.destroyAllWindows()
