import cv2
import os
import numpy as np
import pytesseract
from datetime import datetime
from tkinter import Tk  # otwieranie plikow z komputera
from tkinter.filedialog import askopenfilename
from wykresy import rysujWykres

pytesseract.pytesseract.tesseract_cmd = r"/bin/tesseract"
def addReceipt():
    Tk().withdraw()  # okno pozwalajace na wybor pliku do odczytu
    filename = askopenfilename()
    cwd = os.getcwd()
    text = pytesseract.image_to_string(filename)
    f = open(cwd + "/nowy_paragon.txt", "w")
    f.write(text)
    f.close()
    n = open(cwd + "/nowy_paragon.txt", "r")
    word = "PLN"
    nSplit = n.read().split()
    indeks = 0
    print(nSplit)
    if word in nSplit:
        print('Word Found in Text File')
        indeks = nSplit.index(word)
        print(indeks)
        currentMonth = str(datetime.now().month)
        with open(cwd + "/"+ currentMonth + ".txt", "a+") as file:
            nowaSuma = file.read()
            print(nowaSuma)
            nowaSuma += nSplit[indeks+1]
            file.write(str(nowaSuma))
            print(nowaSuma)
    else:
        print('Word not found in Text File')
    n.close()
    rysujWykres()
