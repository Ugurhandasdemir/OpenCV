import cv2 as cv
import numpy as np

# Belirtilen yoldan resmi oku
img = cv.imread("C:/Users/ugurh/Desktop/a.png")

# Orijinal resmi göster
cv.imshow("Orjinal", img)

# Resmin iki kopyasını yatay olarak birleştir
hor = np.hstack((img,img))

# Yatay olarak birleştirilmiş resmi göster
cv.imshow(" yatay:",hor)

# Resmin iki kopyasını dikey olarak birleştir
ver = np.vstack((img,img))

# Dikey olarak birleştirilmiş resmi göster
cv.imshow("dikey:",ver)
