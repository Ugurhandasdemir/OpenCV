import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("C:/Users/ugurh/Desktop/a.png", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orjinal")

#Erozyon
kernel = np.ones((5,5), dtype=np.uint8)
result = cv.erode(img, kernel, iterations=1)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon")

#Genişleme dilation
result2 = cv.dilate(img, kernel, iterations=1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genişleme")

#white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("whiteNoise")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("noise_img")

#açılma
opening = cv.morphologyEx(noise_img.astype(np.float32),cv.MORPH_OPEN , kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("opening")

#black noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("blackNoise")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img<=-245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("black_noise_img")

#kapatma
closing = cv.morphologyEx(black_noise_img.astype(np.float32),cv.MORPH_CLOSE , kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("closing")

#gradient

gradient = cv.morphologyEx(img.astype(np.float32),cv.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("gradient")



   