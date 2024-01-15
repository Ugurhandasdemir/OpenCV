import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("C:/Users/ugurh/Desktop/a.png",0)
plt.figure(), plt.imshow(img, cmap = "gray")

image , contours , hierarch = cv.findContours(img, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

for i in range(len(contours)):
    #external
    if hierarch[0][i][3] == -1:
        cv.drawContours(external_contour, contours, i, 255, -1)
    else:
        cv.drawContours(internal_contour, contours, i, 255, -1)

plt.figure(), plt.imshow(external_contour, cmap = "gray")
plt.figure(), plt.imshow(internal_contour, cmap = "gray")
