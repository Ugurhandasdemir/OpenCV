import cv2 as cv
import matplotlib.pyplot as plt

# İlk resmi okuyun ve rengini dönüştürün
img1 = cv.imread("C:/Users/ugurh/Desktop/d.jpg")
img1= cv.cvtColor(img1,cv.COLOR_BGR2RGB)

# İkinci resmi okuyun ve rengini dönüştürün
img2 = cv.imread("C:/Users/ugurh/Desktop/e.jpg")
img2= cv.cvtColor(img2,cv.COLOR_BGR2RGB)

# İlk ve ikinci resmi gösterin
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# İlk ve ikinci resmin şeklini yazdırın
print(img1.shape)
print(img2.shape)

# İlk ve ikinci resmi yeniden boyutlandırın
img1 = cv.resize(img1,(180,280))
img2= cv.resize(img2,(180,280))

# Yeniden boyutlandırılmış ilk ve ikinci resmin yeni şeklini yazdırın
print(img1.shape, img2.shape)

# Yeniden boyutlandırılmış ilk ve ikinci resmi gösterin
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# İlk ve ikinci resmi karıştırın
# Karıştırılmış resim, ilk ve ikinci resmin ağırlıklı toplamıdır
blended= cv.addWeighted(src1 =img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)

# Karıştırılmış resmi gösterin
plt.figure()
plt.imshow(blended)
