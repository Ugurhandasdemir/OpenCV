import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/ugurh/Desktop/a.png")
cv.imshow("Orjinal", img)

#yatay
hor =np.hstack((img,img))
cv.imshow(" yatay:",hor)

#dikey
ver = np.vstack((img,img))
cv.imshow("dikey:",ver)
