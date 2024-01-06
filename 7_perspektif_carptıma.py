import cv2 as cv
import numpy as np

# Belirtilen yoldan resmi oku
img = cv.imread("C:/Users/ugurh/Pictures/Screenshots/Ekran görüntüsü 2024-01-05 114412.png")

# Orijinal resmi göster
cv.imshow("deneme",img)

# Perspektif dönüşümü için kaynak ve hedef noktaları belirle
pts1 = np.float32([[152,38],[147,753],[653,26],[656,755]])
pts2 = np.float32([[0,0],[0,500],[400,0],[400,500]])  

# Perspektif dönüşüm matrisini hesapla
matrix = cv.getPerspectiveTransform(pts1, pts2)
print(matrix)

# Perspektif dönüşümünü uygula
imgOutPut = cv.warpPerspective(img, matrix, (400,500))

# Dönüştürülmüş resmi göster
cv.imshow("result", imgOutPut)
