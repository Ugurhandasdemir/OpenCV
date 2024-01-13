import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("rd.png")
img_vis= cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis)

img_hist = cv.calcHist([img], channels= [0], mask= None, histSize=[256], ranges=[0,256])
plt.figure(), plt.plot(img_hist)

color = ("b","g","r")
plt.figure()
for i, c in enumerate(color):
    hist = cv.calcHist([img],channels=[i],mask= None, histSize=[256],ranges=[0,256])
    plt.plot(hist,color= c)
    
    
gg= cv.imread("C:/Users/ugurh/Documents/python/OpenCV/13-)Histogram/gg.jpg")
gg_vis= cv.cvtColor(gg, cv.COLOR_BGR2RGB)
plt.figure(), plt.imshow(gg_vis)

mask =np.zeros(gg.shape[:2], np.uint8)
plt.figure(), plt.imshow(mask, cmap="gray")

mask[500:700,750:1250]=255
plt.figure(), plt.imshow(mask, cmap="gray")

mask_vis =  cv.bitwise_and(gg_vis, gg_vis, mask=mask)
plt.figure(), plt.imshow(mask_vis, cmap="gray")

mask_hist = cv.calcHist([gg], channels=[1], mask=mask, histSize=[256], ranges=[0,256])
plt.figure(), plt.plot(mask_hist)

img1= cv.imread("C:/Users/ugurh/Documents/python/OpenCV/13-)Histogram/clahe_2.jpg")
plt.figure(), plt.imshow(img1,cmap="gray")




































