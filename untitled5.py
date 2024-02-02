import cv2 as cv
import os

files = os.listdir()
print(files)

img_path_list = []

for f in files:
    if f.endswith(".jpg"):
        img_path_list.append(f)
print(img_path_list)

for i in img_path_list:
    print(i)
    image=cv.imread(i)
    cat_gray= cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    detecetor = cv.CascadeClassifier("haarcascade_frontalcatface.xml")
    rects = detecetor.detectMultiScale(cat_gray, scaleFactor= 1.001,minNeighbors=6 )
    
    for(j,(x,y,w,h)) in enumerate(rects):
        cv.rectangle(image,(x,y),(x+w, y+h),(0,255,255),2 )
        cv.putText(image, "kedi {}".format(j+1), (x,y-10), cv.FONT_HERSHEY_COMPLEX, 0.55, (255,255,255),2)
    


    cv.imshow("kedi", image)
    if cv.waitKey(0) & 0xFF  == ord("q") : continue

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if ret:
        face_rect = detecetor.detectMultiScale(frame, minNeighbors=14)
        for (x,y,w,h) in face_rect:
           cv.rectangle(frame, (x,y),(x+w, y+h), (255,255,255),10)
        cv.imshow("Detecey",frame)

    if cv.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv.destroyAllWindows()


