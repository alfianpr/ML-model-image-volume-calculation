import cv2
import numpy as np
from ml_model_telur import predict

with open("android_camera.txt", encoding='utf8') as url:
    url = str(url.readlines()[0])+"/video"


# Fungsi Otsu's Thresholding setelah Gaussian filtering
def threshold(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret1,th1 = cv2.threshold(img,90,255,cv2.THRESH_BINARY)
    #ret1, th1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th1

# Fungsi open morphologi untuk menghilangkan noise
def open_morphology(th3):
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)
    return opening

# While loop to continuously fetching data from the Url
while True:
    cap = cv2.VideoCapture(url)
    ret, img = cap.read()
    show = cv2.resize(img, (500, 300))
    #show = cv2.rotate(show, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("ESC untuk keluar, C double untuk volume", show)
    
    # Press C for calculate the volume
    if cv2.waitKey(0) == ord('c'):
        cv2.imwrite("telur.jpg", img)
        img = cv2.imread("telur.jpg", 0) # Read image

        # Proses thresholding dan morphologi
        th3 = threshold(img)
        opening = open_morphology(th3)

        # Menjumlahkan pixel putih
        pixel_putih = np.sum(opening == 255)
        print ("Jumlah pixel : ", pixel_putih)

        with open("android_camera.txt", encoding='utf8') as jarak:
          jarak = jarak.readlines()[1]
        
        jarak = float(jarak)
        print("jarak (m):", jarak)

        # Menampilkan citra biner
        biner = cv2.resize(opening, (500, 300))
        #biner = cv2.rotate(biner, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("Citra biner", biner)

        print("Sedang memproses...")
        print("Volumenya adalah (cm^3) :", predict(jarak, pixel_putih))

    # Press Esc key to exit
    if cv2.waitKey(0) == 27:
        break

cv2.destroyAllWindows()