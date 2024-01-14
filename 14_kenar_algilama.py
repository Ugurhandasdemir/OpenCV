import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("bb.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

edges = cv.Canny(image = img,threshold1=0, threshold2=255)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

med_val = np.median(img) 
print(med_val)

low = int(max(0,(1-0.33)*med_val))
high = int (min(255,(1+0.33)*med_val))
print(low, high)

edges = cv.Canny(image = img,threshold1=low, threshold2=high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

#blur

blur_img= cv.blur(img, ksize=(5,5))
plt.figure(), plt.imshow(blur_img, cmap="gray"), plt.axis("off")

med_val1 = np.median(blur_img)
low1 = int(max(0,(1-0.33)*med_val1))
high1 = int (min(255,(1+0.33)*med_val1))

edges_blur = cv.Canny(image = blur_img, threshold1=low1, threshold2=high1)
plt.figure(), plt.imshow(edges_blur,cmap="gray"),plt.axis("off")



