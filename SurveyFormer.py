from four_point_transform import four_point_transform,line_intersect,find_colums,find_rows
from scipy import ndimage 
import cv2
import imutils
import numpy as np 
from numpy import genfromtxt
from skimage import filters as anything
import pandas as pd
import matplotlib.pyplot as plt 
import PIL 
import os
from pathlib import Path
import csv
from enum import Enum

class OrderOfForm(Enum):
        Ascending = 200
        Descending = 300
        #Descending มากไปน้อย

class SurveyFormer:
    def __init__(self,path,order):
        self.symbol_coordinate = [] 
        self.path = path
        self.root = os.path.dirname(os.path.realpath(__file__))
        self.detector = cv2.CascadeClassifier(self.root + os.path.sep + 'src/cascade-1.xml')
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.color = (0,255,0)
        self.order = order
        self.dict = self.newrecord()

    def convert2GCBE(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(11,11))
        cl1 = clahe.apply(gray)
        gray = cv2.GaussianBlur(cl1, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)
        return edged

    def recognizer(self):
        self.image = cv2.imread(self.path)
        self.ratio = self.image.shape[0] / 500.0
        self.orig = self.image.copy()
        self.image = imutils.resize(self.image, height = 500)
        self.gray = self.convert2GCBE(self.image)
        self.warped = self.findMaxpaperINimage()
        self.table = self.findTableINpaper(self.warped)
        self.origTable = self.table.copy()
        self.table = self.normolize()
        self.result = self.detechSymbol(self.table)
        return self.result

    def findMaxpaperINimage(self):
        # เมื่อหาขอบภาพแล้ว ใช้ findcontours เพื่อตีกรอบภาพโดยใช้ contourArea
        cnts = cv2.findContours(self.gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
        # ลูปหารูปทรง contours
        for c in cnts:
            # คำนวณหาวัตถุที่มีขนาดใหญ่สุดในภาพ
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # เมื่อมีมุม 4 มุมให้มีค่า approx และตีกรอบเมื่อตีกรอบได้แล้วให้หยุดการทำงาน
            if len(approx) == 4:
                screenCnt = approx
                break
        # หาขอบ หาคอนทัวร์ที่มีลักษณะสี่เหลี่ยม เพื่อส่งไปให้ four_point_transform ทำการเพอร์เพ็กทีฟ = การดึงค่าให้เป็นจุด 
        rect,warped = four_point_transform(self.orig, screenCnt.reshape(4, 2) * self.ratio)
        # แปลงภาพเป็น gray แล้วทำการ threshold
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        T = anything.threshold_local(warped, 11, offset = 10, method = "gaussian")
        warped = (warped > T).astype("uint8") * 255
        return warped

    def findTableINpaper(self,warped):
        gauss = cv2.adaptiveThreshold(warped,200,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 0)
        ret,thresh = cv2.threshold(gauss,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST ,cv2.CHAIN_APPROX_SIMPLE)
        c = max(cnts, key = cv2.contourArea)
        (x, y, w, h) = cv2.boundingRect(c)
        # แล้วเลือกวัตถุโดยให้ y+h และ x+w เป็น 4 ตัวกำหนดพิกัดภาพ
        crop_img = warped[y:y+h, x:x+w]
        return crop_img

    def normolize(self):
        clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(11,11))
        cl1 = clahe.apply(self.table)
        kernel = np.ones((2,2), np.uint8) 
        cl1 = cv2.erode(cl1, kernel, iterations=1) 
        cl1 = cv2.dilate(cl1, kernel, iterations=1) 
        return cl1

    def newrecord(self):
        if self.order is OrderOfForm.Descending:
            return {1:0,2:0,3:0,4:0,5:0}
        else:
            return {5:0,4:0,3:0,2:0,1:0}

    def isFileOutput(self):
        return os.path.isfile(self.root + os.path.sep + 'src/export.txt')


    def detechSymbol(self,roi):
        if not self.isFileOutput():
            Path(self.root + os.path.sep + 'src/export.txt').touch()
            with open(self.root + os.path.sep + 'src/export.txt', mode='a+') as export:
                export.write("no,point\n")
                export.close()
        with open(self.root + os.path.sep + 'src/export.txt', mode='a+') as export:
            symbol = self.detector.detectMultiScale(roi,3.1, 4)
            header = [(483,46),(523,46),(563,46),(601,46),(641,46)]
            score = 0
            for i,(x, y, w, h) in enumerate(symbol):
                cv2.rectangle(self.origTable, (x,y), (x+w,y+h),(50,255,50), 2)
                px,py = int(x+w/2),int(y+h/2)
                cv2.circle(self.origTable,(px, py), 2,(50,255,50), -1)
                index = find_colums(x,w)
                index_y = find_rows(y,h)
                cv2.putText(self.origTable,str(index)+str(",{}".format(index_y)), (x+15,y+2), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0, 0, 255))
                score += index
                d1 = {index:self.dict.get(index,0)+1}
                self.dict.update(d1)
                export.write(f"{index_y},{index}\n")
            print(self.dict)
            export.close()
            self.dict = self.newrecord()
        return self.origTable

