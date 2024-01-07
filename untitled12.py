import cv2 as cv 
import matplotlib.pyplot as plt

img = cv.imread("C:/Users/ugurh/Desktop/d.jpg")
img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()


#eşikleme
_, tresh_img = cv.threshold(img, thresh=60, maxval=255, type=cv.THRESH_BINARY)

plt.figure()
plt.imshow(tresh_img, cmap="gray")
plt.axis("off")
plt.show()

#uyarlamalı eşik değeri
tresh_img2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,8)

plt.figure()
plt.imshow(tresh_img2, cmap="gray")
plt.axis("off")
plt.show()
