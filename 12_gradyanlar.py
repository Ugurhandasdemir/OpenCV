import cv2 as cv
import matplotlib.pyplot as plt

# Resmi gri tonlamalı olarak oku
img = cv.imread("C:/Users/ugurh/Documents/python/OpenCV/12-)Gradyanlar/a.png", 0)

# Resmi çiz
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("sudoku")

# x gradyanını hesapla
sobelx= cv.Sobel(img, ddepth=cv.CV_16S, dx=1, dy=0, ksize=5)
plt.figure(), plt.imshow(sobelx, cmap="gray"), plt.axis("off"), plt.title("sobelx") 

# y gradyanını hesapla
sobely= cv.Sobel(img, ddepth=cv.CV_16S, dx=0, dy=1, ksize=5)
plt.figure(), plt.imshow(sobely, cmap="gray"), plt.axis("off"), plt.title("sobel y")

# Laplasyen gradyanını hesapla
laplacion= cv.Laplacian(img, ddepth=cv.CV_16S)
plt.figure(), plt.imshow(laplacion, cmap="gray"), plt.axis("off"), plt.title("laplacion")
