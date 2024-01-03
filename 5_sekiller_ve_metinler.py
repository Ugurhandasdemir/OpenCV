import cv2 as cv
import numpy as np
#Şekiller ve metin

#resim oluştur
img = np.zeros((512,512,3),np.uint8) # siyah bir resim
# Siyah bir resim oluşturur
print(img.shape)

cv.imshow("Siyah",img)

#çizgi
#(resim,başlangıc noktası, bitiş noktası, renk ,kalınlık)
cv.line(img,(100,100),(300,300),(0,255,0),3) #BGR
# Bir çizgi çizer
cv.imshow("Cizgi", img)

#dikdörtgen
cv.rectangle(img, (122,122),(222,222),(255,0,0),cv.FILLED)
# Bir dikdörtgen çizer
cv.imshow("Diktorgen", img)

#Çember
#(resim,merkez,yarı çap, renk)
cv.circle(img, (333,333), 20, (0,0,255),cv.FILLED)
# Bir çember çizer
cv.imshow("Cember", img)

#text
#(resim,başlangıç noktası,font,kalınlığı,renk)
cv.putText(img, "Deneme", (322,322), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
# Metin yazdırır
cv.imshow("yazı", img)
