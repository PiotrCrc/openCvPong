import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from ponggame import ponggame

def nothing(x):
    pass

if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    first = True

    cv.namedWindow('image')
    cv.createTrackbar('Value 1', 'image', 0, 255, nothing)
    cv.createTrackbar('Value 2', 'image', 0, 255, nothing)



    while(1):

        _, frame = cap.read()

        value1 = cv.getTrackbarPos('Value 1', 'image')
        value2 = cv.getTrackbarPos('Value 2', 'image')

        src_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        after_cv = frame

        ### Threshold https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
        _, after_cv = cv.threshold(src_gray, value1, value2, cv.THRESH_TOZERO)
        # _, after_cv = cv.threshold(src_gray, value1, value2, cv.THRESH_BINARY_INV)

        ### image smooting - avreging https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html
        # if first:
        #     cv.setTrackbarPos('Value 1', 'image', 110)
        # kernel_size = int((value1 // 25.5)*2+1)
        # kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)
        # dst = cv.filter2D(frame, -1, kernel)
        # after_cv = dst

        ### Color thresholding https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html
        # if first:
        #     cv.setTrackbarPos('Value 1', 'image', 110)
        #     cv.setTrackbarPos('Value 2', 'image', 255)
        #
        # frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # kernel = np.ones((5, 5), np.float32) / 25
        # dst = cv.filter2D(frame_HSV, -1, kernel)
        # mask = cv.inRange(dst, (value1, 20, value2), (value1+50, 255, value2+100))
        # after_cv = cv.bitwise_and(frame,frame,mask=mask)

        ### Canny edge detection https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
        # after_cv = cv.Canny(src_gray, value1, value2)

        ### Template matching https://docs.opencv.org/3.4/d4/dc6/tutorial_py_template_matching.html
        # if first:
        #     template = cv.imread('photo.jpeg', 0)
        #     w, h = template.shape[::-1]
        # res = cv.matchTemplate(src_gray, template, cv.TM_CCOEFF)
        # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # top_left = max_loc
        # bottom_right = (top_left[0] + w, top_left[1] + h)
        # after_cv = frame
        # cv.rectangle(after_cv, top_left, bottom_right, (255,0,0), 2)

        ### Polygon detection https://www.geeksforgeeks.org/python-detect-polygons-in-an-image-using-opencv/
        # if first:
        #     cv.setTrackbarPos('Value 1', 'image', 110)
        #     cv.setTrackbarPos('Value 2', 'image', 255)
        # _, threshold = cv.threshold(src_gray, value1, value2,
        #                              cv.THRESH_BINARY)
        # contours, _ = cv.findContours(threshold, cv.RETR_TREE,
        #                                cv.CHAIN_APPROX_SIMPLE)
        # for cnt in contours:
        #     approx = cv.approxPolyDP(cnt,
        #                               0.009 * cv.arcLength(cnt, True), True)
        #     area = cv.contourArea(cnt)
        #     if ( area > 200 ) and (len(approx) < 30):
        #         cv.drawContours(after_cv, [approx], 0, (0, 0, 255), 2)


        cv.imshow('image', after_cv)

        ### pong
        #
        # if first:
        #     new_game = ponggame(frame.shape[0],frame.shape[1])
        #
        # kernel = np.ones((5, 5), np.float32) / 25
        # scr_gray = cv.filter2D(src_gray, -1, kernel)
        # _, thresh4 = cv.threshold(src_gray, value1, 255, cv.THRESH_BINARY_INV)
        #
        # for _ in range(5):
        #     new_game.nastpena_klatka(thresh4)
        # new_game.rysuj_pilke(thresh4)
        # cv.imshow('2', thresh4)

        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
        first = False

    cv.destroyAllWindows()