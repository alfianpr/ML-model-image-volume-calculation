import cv2
import numpy as np
import requests
import imutils
from ml_model_telur import *

with open("android_camera.txt", encoding='utf8') as url:
    url = url.readlines()[0]

url = str(url)+"/shot.jpg"

# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Telur_cam", img)
  
    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break

cv2.imwrite("telur.jpg", img)
cv2.destroyAllWindows()


img = cv2.imread("telur.jpg", 0)
# Otsu's thresholding setelah Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Open Morphology untuk menghilangkan noise
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)

pixel_putih = np.sum(opening == 255)
print ("Jumlah pixel : ", pixel_putih)

jarak = input("Input jarak (meter) :\n")
jarak = float(jarak)
text = predict(jarak, pixel_putih)

print("Volumenya adalah (cm^3) :", text)
