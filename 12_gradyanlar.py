import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("C:/Users/ugurh/Documents/python/OpenCV/12-)Gradyanlar/a.png", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("sudoku")

# x gradyan
sobelx= cv.Sobel(img, ddepth=cv.CV_16S, dx=1, dy=0, ksize=5)
plt.figure(), plt.imshow(sobelx, cmap="gray"), plt.axis("off"), plt.title("sobelx") 

# y gradyan
sobely= cv.Sobel(img, ddepth=cv.CV_16S, dx=0, dy=1, ksize=5)
plt.figure(), plt.imshow(sobely, cmap="gray"), plt.axis("off"), plt.title("sobel y")

# laplacion gradyan
laplacion= cv.Laplacian(img, ddepth=cv.CV_16S)
plt.figure(), plt.imshow(laplacion, cmap="gray"), plt.axis("off"), plt.title("laplacion")























