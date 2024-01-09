import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Görüntüyü gri tonlamalı olarak oku
img = cv.imread("C:/Users/ugurh/Desktop/a.png", 0)

# Orjinal görüntüyü göster
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orjinal")

# Erozyon ve genişleme için çekirdeği tanımla
kernel = np.ones((5,5), dtype=np.uint8)

# Görüntü üzerinde erozyon işlemi gerçekleştir
result = cv.erode(img, kernel, iterations=1)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon")

# Görüntü üzerinde genişleme işlemi gerçekleştir
result2 = cv.dilate(img, kernel, iterations=1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genişleme")

# Beyaz gürültü oluştur
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("whiteNoise")

# Görüntüye beyaz gürültü ekle
noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("noise_img")

# Gürültüyü kaldırmak için açma işlemi gerçekleştir
opening = cv.morphologyEx(noise_img.astype(np.float32),cv.MORPH_OPEN , kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("opening")

# Siyah gürültü oluştur
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("blackNoise")

# Görüntüye siyah gürültü ekle
black_noise_img = blackNoise + img
black_noise_img[black_noise_img<=-245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("black_noise_img")

# Gürültüyü kaldırmak için kapatma işlemi gerçekleştir
closing = cv.morphologyEx(black_noise_img.astype(np.float32),cv.MORPH_CLOSE , kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("closing")

# Kenarları vurgulamak için gradyan işlemi gerçekleştir
gradient = cv.morphologyEx(img.astype(np.float32),cv.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("gradient")
