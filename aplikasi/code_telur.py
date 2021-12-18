import cv2
import numpy as np
from ml_model_telur import *

with open("android_camera.txt", encoding='utf8') as url:
    url = str(url.readlines()[0])+"/video"


# While loop to continuously fetching data from the Url
while True:
    cap = cv2.VideoCapture(url)
    ret, img = cap.read()
    show = cv2.resize(img, (600, 400))
    cv2.imshow("Tekan ESC untuk keluar, tekan C dua kali untuk volume", show)
    
    # Press C for calculate the volume
    if cv2.waitKey(0) == ord('c'):
        cv2.imwrite("telur.jpg", img)
        img = cv2.imread("telur.jpg", 0) # Read image

        # Otsu's thresholding setelah Gaussian filtering
        blur = cv2.GaussianBlur(img,(5,5),0)
        ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # Open Morphology untuk menghilangkan noise
        kernel = np.ones((5,5),np.uint8)
        opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)

        pixel_putih = np.sum(opening == 255)
        print ("Jumlah pixel : ", pixel_putih)

        with open("android_camera.txt", encoding='utf8') as jarak:
          jarak = jarak.readlines()[1]
        jarak = float(jarak)
        print("jarak (m):", jarak)

        print("Sedang memproses...")
        text = predict(pixel_putih, jarak)

        print("Volumenya adalah (cm^3) :", text)

    # Press Esc key to exit
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()