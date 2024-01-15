import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("a.png",0)
img = np.float32(img)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# Harris corner detection
dst = cv.cornerHarris(img, blockSize=2, ksize=3, k=0.04)
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

dst = cv.dilate(dst, None)
img[dst > 0.2*dst.max()] = 1
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# Shi-Tomasi corner detection
img = cv.imread("a.png",0)
img = np.float32(img)
corners = cv.goodFeaturesToTrack(img, 100, 0.01,10)
corners = np.int64(corners)

for i in corners:
    x,y =  i.ravel()
    cv.circle(img,(x,y),3,(125,125,125),cv.FILLED)
    
plt.imshow(img), plt.axis("off")
