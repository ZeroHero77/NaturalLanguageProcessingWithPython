# -*- coding: utf-8 -*-
"""

Created on Mon Sep  7 19:42:31 2020

@author: William Gbadebo E Smith


"""

__author__ = "William Gbadebo E Smith"
__copyright__ = "Copyright 2020, William Gbadebo E Smith"

import os
# import fitz
#import glob
#import tensorflow 
#import torch 
import PyPDF2

def main():
    stopworder(x)

def stopworder(x):
    str(x).replace('1/18','')

folderFx = os.chdir(r'C:\Users\wgesm\Documents\ws\hackerearth\machinelearning\TestData')

folderFx


folderFx = os.listdir(r'C:\Users\wgesm\Documents\ws\hackerearth\machinelearning\TestData')

folderFx

fileobj = open('Scripts_Goblet of Fire.pdf', 'rb')
pdfobj = PyPDF2.PdfFileReader(fileobj)

# for i in range(0,18,1):
#     pdfread1 = pdfobj.getPage(i) 

pdfread0 = pdfobj.getPage(0)
pdfread1 = pdfobj.getPage(1)
pdfread2 = pdfobj.getPage(2)
pdfread3 = pdfobj.getPage(3)
pdfread4 = pdfobj.getPage(4)
pdfread5 = pdfobj.getPage(5)
pdfread6 = pdfobj.getPage(6)
pdfread7 = pdfobj.getPage(7)
pdfread8 = pdfobj.getPage(8)
pdfread9 = pdfobj.getPage(9)
pdfread10 = pdfobj.getPage(10)
pdfread11 = pdfobj.getPage(11)
pdfread12 = pdfobj.getPage(12)
pdfread13 = pdfobj.getPage(13)
pdfread14 = pdfobj.getPage(14)
pdfread15 = pdfobj.getPage(15)
pdfread16 = pdfobj.getPage(16)
pdfread17 = pdfobj.getPage(17)


file0 = pdfread0.extractText() 
file0 += '\n'+pdfread1.extractText()
file0 += '\n'+pdfread2.extractText()
file0 += '\n'+pdfread3.extractText()
file0 += '\n'+pdfread4.extractText()
file0 += '\n'+pdfread5.extractText()
file0 += '\n'+pdfread6.extractText()
file0 += '\n'+pdfread7.extractText()
file0 += '\n'+pdfread8.extractText()
file0 += '\n'+pdfread9.extractText()
file0 += '\n'+pdfread10.extractText()
file0 += '\n'+pdfread11.extractText()
file0 += '\n'+pdfread12.extractText()
file0 += '\n'+pdfread13.extractText()
file0 += '\n'+pdfread14.extractText()
file0 += '\n'+pdfread15.extractText()
file0 += '\n'+pdfread16.extractText()
file0 += '\n'+pdfread17.extractText()
file0 = file0.replace('1/18','').replace('2/18','').replace('3/18','').replace('4/18','').replace('5/18','').replace('6/18','').replace('7/18','').replace('8/18','').replace('9/18','').replace('10/18','').replace('11/18','').replace('12/18','').replace('13/18','').replace('14/18','').replace('15/18','').replace('16/18','').replace('17/18','').replace('18/18','')

with open("testDataFile.txt", 'w+') as f:
    f.write(file0)
    f.close()
    






