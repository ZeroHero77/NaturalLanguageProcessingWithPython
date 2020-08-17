import os
import fitz
import glob

print("starting convert pdf to png...")

os.chdir(r'C:\Users\McSmith\Documents\Will\Code\NLP\Bojacks\Dataset\Test')


folderFx = os.listdir(r'C:\Users\McSmith\Documents\Will\Code\NLP\Bojacks\Dataset\Test')


def atenmill():
    return int(10000000)

def a0():
    return int(0)

def a1():
    return int(1)



for i in folderFx:
    THIS_FOLDER = os.path.dirname(os.path.abspath(i))
    my_file = os.path.join(THIS_FOLDER, str(i))
    list1 = fitz.open(i)
   

    for images in list1.getPageImageList(0):
        check = images[0]
        firstpicture = fitz.Pixmap(list1, check)
        lastpicture = fitz.Pixmap(fitz.csGRAY, firstpicture)
        lastpicture.writePNG(str(i)[0:-4]+".png")
        firstpicturepicture = None
        lastpicture= None

print("convert pdf to png complete...")

print("one minute...")

print("starting resize images...")
print("starting print text from images")

folderFx

import pytesseract 
from PIL import Image
import csv

def returns_path(): 
    return r'C:\Users\McSmith\Documents\Will\Code\NLP\Bojacks\Dataset\Test\TestAB.csv'

filex = open(returns_path(), 'w', newline='\n', encoding='utf-8')
writer = csv.writer(filex)
writer.writerow(["FileName", "Total Amount"])

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

FileName = []
sorterX = []
sortedX = str()

Total = str()


folderFx


# LengthX = int(348) + WidthX = int(348) == 74.40988
# LengthX = int(450) + WidthX = int(550) == 75.32320
# LengthX = int(1150) + WidthX = int(1350) == 73.83350
# LengthX = int(550) + WidthX = int(650) == 73.28281
# LengthX = int(444) + WidthX = int(333) == 81.75175
# LengthX = int(777) + WidthX = int(666) == 90.12867
# LengthX = int(777) * 1.01 + WidthX = int(666) * 1.01 == 72.49086
# LengthX = int(777) * 1.02 + WidthX = int(666) * 1.02 == 

import re

def valX():
    return float(1.1666666667)

def MultiplierX():
    return float(1.00)

def WidthX():
    return int(int(1150) * MultiplierX())

def LengthX():
    return int((round((WidthX()*valX() * MultiplierX()),0)))

def enumeralX():
    return int(131)

def totalrecords():
    return int(70)

def beginX():
    return int(0)

def stepX(): 
    return int(1)
 
def regexX():
    return "[0-9]+[ 0-9][.][ 0-9][0-9]+"

picturesappended = []
resized_pics  = []
try: 
    
    def globX(): 
        return glob.glob('C:/Users/McSmith/Documents/Will/Code/NLP/Bojacks/Dataset/Test/*.png')
    
    for j in globX():
        FileName.append(j)
        pictures = Image.open(j)
        picturesappended += [pictures]
        # pictures.show()
    
    for pix1 in range(beginX(),totalrecords(),stepX()):
        picasso = picturesappended[pix1].resize((LengthX(),WidthX()))
        picasso.save(("TE_"+str(enumeralX()+pix1)+".png"))
        
                 
    for jjj in globX():
        FileName = jjj[jjj.find("TE_"):-4]
        stringtexti = pytesseract.image_to_string(jjj)
        stringtextii = stringtexti
        stringtext = re.sub("\'", "", re.sub(" ", "", re.sub("\]", "", re.sub("\[", "", str(stringtextii)))))
        matchesX = re.findall(regexX(), stringtext)
        sorterX = list(map(float,matchesX))
        print(FileName, sorterX, len(sorterX))
        
        if len(matchesX) ==1: sortedX = float(sorterX[0])
        elif len(matchesX) >1: sortedX = float(sorterX[len(sorterX)-1])
        else: sortedX = float(0.00)
    
        Total = sortedX
         
        writer.writerow([FileName, Total])

except EOFError: pass 
    
filex.close()
print("resize images complete")
print("print text from images complete...")
print("Finir") 
