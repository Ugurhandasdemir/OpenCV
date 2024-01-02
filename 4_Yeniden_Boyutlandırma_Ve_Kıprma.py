import cv2 as cv

img = cv.imread("C:/Users/ugurh/Desktop/c.jpg", 0)
print("Resim bpyutu: ",img.shape)
cv.imshow("orjinal", img)

imgResize =cv.resize(img, (800,800))
print("Yeni resim boyutu: ", imgResize.shape)
cv.imshow("Yeni boyut", imgResize)

#kırma

imgCropped = img[:321,:349] # 
cv.imshow("Kırpılmıs", imgCropped)