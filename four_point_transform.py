import numpy as np
from scipy import ndimage
import PIL
import numpy as np
import argparse
import cv2
import imutils
import matplotlib.pyplot as plt

def find_colums(x,w):
	if abs((x+w) - 328) <= 14:
		index = 5
	elif abs((x+w) - 356) <= 14:
		index = 4
	elif abs((x+w) - 382) <= 14:
		index = 3
	elif abs((x+w) - 409) <= 14:
		index = 2
	elif abs((x+w) - 437) <= 14:
		index = 1
	else:
		index = []
	# print (index)
	return index

def find_rows(y,h):
	index1 = 0
	if abs((y+h) - 62) <= 13:
		index1 = 1
	elif abs((y+h) - 80) <= 13:
		index1 = 2
	elif abs((y+h) - 115) <= 13:
		index1 = 3
	elif abs((y+h) - 133) <= 13:
		index1 = 4
	elif abs((y+h) - 152) <= 13:
		index1 = 5
	elif abs((y+h) - 185) <= 13:
		index1 = 6
	elif abs((y+h) - 203) <= 20:
		index1 = 7
	elif abs((y+h) - 220) <= 20:
		index1 = 8
	elif abs((y+h) - 257) <= 20:
		index1 = 9
	elif abs((y+h) - 275) <= 20:
		index1 = 10
	elif abs((y+h) - 295) <= 20:
		index1 = 11
	else:
		index1 = 0
	return index1

def order_points(pts):
	# ใช้ดึงจุด 4 จุดของรูปมา
	# สร้างตัวแปร rect มีค่า 4 แถว 2 คอลลัม อาเรย์ 2 มิติ
	rect = np.zeros((4, 2), dtype = "float32")
 
	s = pts.sum(axis = 1)
	print(s)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
 
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	return rect
	
def four_point_transform(image, pts):
	# กำหนด rect ให้เป็น 4 ค่า
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	# compute the width of the new image, which will be the
	# maximum distance between bottom-right and bottom-left
	# x-coordiates or the top-right and top-left x-coordinates
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	# compute the height of the new image, which will be the
	# maximum distance between the top-right and bottom-right
	# y-coordinates or the top-left and bottom-left y-coordinates
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	# now that we have the dimensions of the new image, construct
	# the set of destination points to obtain a "birds eye view",
	# (i.e. top-down view) of the image, again specifying points
	# in the top-left, top-right, bottom-right, and bottom-left
	# order
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	# compute the perspective transform matrix and then apply it
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	# return the warped image
	return rect,warped










# Function Lineintersect
def line_intersect(x1,y1,x2,y2,x3,y3,x4,y4):	
	px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
	py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
	return int(px),int(py)

    # rect[0][0]  x1
	# rect[0][1]  y1
	# rect[1][0]  x2
	# rect[1][1]  y2
	# rect[2][0]  x3
	# rect[2][1]  y3
	# rect[3][0]  x4
	# rect[3][1]  y4

