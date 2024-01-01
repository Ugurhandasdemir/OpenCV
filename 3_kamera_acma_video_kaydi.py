import cv2 as cv

# Video yakalama nesnesi oluşturuluyor
cap = cv.VideoCapture(0)

# Video genişliği ve yüksekliği alınıyor
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Genişlik ve yükseklik yazdırılıyor
print(width , height)

# Video yazıcı nesnesi oluşturuluyor
writer = cv.VideoWriter("Deneme1.mp4", cv.VideoWriter_fourcc(*"DIVX"),30,(width, height))

# Video çerçeveleri okunuyor ve yazılıyor
while True:
    ret, frame = cap.read()  # Çerçeve okunuyor
    cv.imshow("Deneme1", frame)  # Çerçeve gösteriliyor
    
    writer.write(frame)  # Çerçeve yazılıyor
    
    # 'q' tuşuna basıldığında döngüden çıkılıyor
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    
# Video yakalama ve yazıcı nesneleri serbest bırakılıyor
cap.release()
writer.release()

# Tüm OpenCV pencereleri kapatılıyor
cv.destroyAllWindows()
