#%% Resim içe aktarmak

import cv2

img =cv2.imread("C:\\Users\\ugurh\\Desktop\\a.jpg",0)

cv2.imshow("ilk resim",img)

k = cv2.waitKey(0) &0xFF

if k == ord("k"):
    cv2.destroyAllWindows()
elif k == ord("g"):
    cv2.imwrite("onepiece_gray.png", img)
    cv2.destroyAllWindows()

#%% Video ice aktarma