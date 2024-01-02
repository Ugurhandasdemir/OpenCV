import cv2 as cv

# Resmi gri tonlamalı modda oku
img = cv.imread("C:/Users/ugurh/Desktop/c.jpg", 0)

# Orijinal resim boyutunu yazdır
print("Resim bpyutu: ",img.shape)

# Orijinal resmi göster
cv.imshow("orjinal", img)

# Resmi 800x800 boyutuna yeniden boyutlandır
imgResize =cv.resize(img, (800,800))

# Yeni resim boyutunu yazdır
print("Yeni resim boyutu: ", imgResize.shape)

# Yeniden boyutlandırılmış resmi göster
cv.imshow("Yeni boyut", imgResize)

# Resmi kırp
imgCropped = img[:321,:349] # 

# Kırpılmış resmi göster
cv.imshow("Kırpılmıs", imgCropped)
