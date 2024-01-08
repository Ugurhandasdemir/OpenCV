import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Resmi oku ve RGB'ye dönüştür
img = cv.imread("C:/Users/ugurh/Desktop/nyc.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Orjinal resmi göster
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Orginal"), plt.show()

# Ortalama bulanıklaştırma yöntemi
dst2 = cv.blur(img, ksize=(3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("Ortalama blur")

# Gaussian blur
gb = cv.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gauss Blur"), plt.show()

# Medyan blur
mb=cv.medianBlur(img, ksize=3)
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("MEdyan bulur"), plt.show()

# Gaussian gürültü fonksiyonu
def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss= np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image+ gauss
    
    return noisy

# Resmi yeniden oku ve RGB'ye dönüştür
img = cv.imread("C:/Users/ugurh/Desktop/nyc.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)/225
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Orginal"), plt.show()

# Gaussian gürültü eklenmiş resmi göster
gaussianNoiseImage = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoiseImage), plt.axis("off"), plt.title("gaussianNoiseImage"), plt.show()

# Gaussian blur uygula
gb2 = cv.GaussianBlur(gaussianNoiseImage, ksize=(3,3), sigmaX=7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("with Gauss Blur"), plt.show()

# Salt & Pepper gürültü fonksiyonu
def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy= np.copy(image)
    
    # Salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p)
    cords=[np.random.randint(0,i-1,int(num_salt))for i in image.size]
    noisy[cords] = 1

    # Pepper siyah
    num_pepper = np.ceil(amount * image.size * (1-s_vs_p))
    cords=[np.random.randint(0,i-1,int(num_pepper))for i in image.size]
    noisy[cords] = 0

    return noisy

# Salt & Pepper gürültü eklenmiş resmi göster
spImage = saltPepperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("spImage"), plt.show()

# Medyan blur uygula
mb2=cv.medianBlur(spImage.astype(np.float32), ksize=3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with MEdyan bulur"), plt.show()
