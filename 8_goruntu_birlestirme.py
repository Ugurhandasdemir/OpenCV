import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("C:/Users/ugurh/Desktop/d.jpg")
img1= cv.cvtColor(img1,cv.COLOR_BGR2RGB)

img2 = cv.imread("C:/Users/ugurh/Desktop/e.jpg")
img2= cv.cvtColor(img2,cv.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1 = cv.resize(img1,(180,280))
img2= cv.resize(img2,(180,280))

print(img1.shape, img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karıştırılmış resim = alpha*img1 + beta*img2

blended= cv.addWeighted(src1 =img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended)
