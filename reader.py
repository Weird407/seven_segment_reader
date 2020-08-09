import cv2
import numpy as np
import sys
import os
import csv

import scratch
import find_seven
import select_digit


#input variables
dir_str = 'folder_dir'
outfile = 'out.csv'
#target temp and where the decimals are
target = 100
decimalpos = 1
#For light correction
alpha = 0.6
beta = 5
#For troubleshooting
TroubleShoot= False

#initialize
first = True
Temperature = []
scale = 4

def col2bin(image):
    #Lower contrast to correct overlighting
    img = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    #Convert to greyscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Convert to Binary
    thresh = 128
    bin_img = cv2.threshold(grey, thresh, 255, cv2.THRESH_BINARY)[1]
    return bin_img

def gettemp(data, decim):
    T = ""
    if data:
        for i in np.arange(np.size(data)-decim):
            if data[i] != "":
                T = T + data[i]
        if decim >0:
            T=T+"."
            for i in np.flip(np.arange(decim))+1:
                T = T + data[-i]
    return T

#Loop over files in folder
dir = os.fsencode(dir_str)
for filename in os.listdir(dir):
    filename = filename.decode("utf-8")
    filename = dir_str+"/" + filename

    #First figure out useful information
    if first:
        #Obtain image
        image = cv2.imread(filename)
        #Obtain cropping region
        c = scratch.Cropper(image)
        c.crop()
        cropcor = c._coords
        #Crop
        (x1, y1), (x2, y2) = c._coords
        cropped = c._image[y1:y2, x1:x2]

        #resize
        h = scale*np.size(cropped,0)
        w = scale*np.size(cropped,1)
        cropped2 = cv2.resize(cropped,(w,h))
        #Find position of 7 segments, as many as user adds
        d = find_seven.finder(cropped2)
        d.find_segment()
        pos_o = d._coords
        #scale down due to scaling
        pos = tuple(tuple(int(i / scale) for i in inner) for inner in pos_o)

        #Convert to Binary
        bin_img = col2bin(cropped)
        #Show during checking
        if TroubleShoot:
            cv2.imshow('binary test',bin_img)
            cv2.waitKey(0)
        #Read segment values
        out = select_digit.read_seg(bin_img,pos)

        #Convert to temperature
        temp = gettemp(out,decimalpos)
        #Save value
        #print(temp,type(temp))
        Temperature.append(temp)

        first = False
    else:
        #Obtain image
        image = cv2.imread(filename)
        #Crop
        cropped = image[y1:y2, x1:x2]
        #Convert to Binary
        bin_img = col2bin(cropped)
        #Show during checking
        if TroubleShoot:
            cv2.imshow('binary test',bin_img)
            cv2.waitKey(0)
        #Read segment values
        out = select_digit.read_seg(bin_img,pos)
        temp = gettemp(out,decimalpos)
        #Save value
        #print(temp)
        Temperature.append(temp)

#todo: output a file
rows = zip(Temperature)
with open(outfile, "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
