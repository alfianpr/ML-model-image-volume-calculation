import tkinter as tk
from PIL import Image, ImageTk
import cv2
from ml_model_beras import predict
#from ml_model_telur import predict
#from code_beras import *
#from code_telur import *
import numpy as np


# Fungsi Otsu's Thresholding setelah Gaussian filtering
def threshold(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3, th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th3

# Fungsi open morphologi untuk menghilangkan noise
def open_morphology(th3):
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, kernel)
    return opening

frame = tk.Tk()
frame.title("volume")
frame.geometry('900x400')

with open("android_camera.txt", encoding='utf8') as url:
    url = str(url.readlines()[0])+"/video"

def proses_beras():
    global pixel_putih
    #input_jarak = input_jarak.get(1.0, tk.END+"-1c")

    cap = cv2.VideoCapture(url)

    ret, img = cap.read()
    cv2.imwrite("beras.jpg", img)
    show = cv2.resize(img, (300, 200))
    show = cv2.rotate(show, cv2.ROTATE_90_COUNTERCLOCKWISE)
    show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)


    #cv2.imwrite("beras.jpg", img)
    img = cv2.imread("beras.jpg", 0) # Read image

    # Proses thresholding dan morphologi
    th3 = threshold(img)
    opening = open_morphology(th3)

    show = Image.fromarray(show)
    show = ImageTk.PhotoImage(show)
    lbl_color.imgtk = show
    lbl_color.configure(image=show)

    biner = cv2.resize(opening, (300, 200))
    biner = cv2.rotate(biner, cv2.ROTATE_90_COUNTERCLOCKWISE)
    biner = Image.fromarray(biner)
    biner = ImageTk.PhotoImage(biner)
    lbl_thresh.imgtk = biner
    lbl_thresh.configure(image=biner)

    # Menjumlahkan pixel putih
    jumlah_pixel= np.sum(opening == 255)
    pixel_putih.set(jumlah_pixel)
    #lbl_pixel.config(text=jumlah_pixel)
    #lbl_pixel["text"] = jumlah_pixel

pixel_putih = tk.IntVar()

input_jarak=tk.Text(frame, height = 2, width = 20)
input_jarak.pack()

printButton = tk.Button(frame, text = "beras", 
                        command = proses_beras)
printButton.pack()

lbl_color = tk.Label(frame, text = "")
lbl_color.pack(side="left", expand="yes", padx="10", pady="10")

lbl_thresh = tk.Label(frame, text = "")
lbl_thresh.pack(side="right", expand="yes", padx="10", pady="10")

lbl_pixel = tk.Label(
                    frame, 
                    textvariable=str(pixel_putih),
                    #text="jumlah pixel"
)
lbl_pixel.pack(padx="10", pady="10")

frame.mainloop()