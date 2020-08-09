import cv2
import numpy as np

DIGITS_LOOKUP = {
	(0, 0, 0, 0, 0, 0, 0): "",
	(1, 1, 1, 0, 1, 1, 1): "0",
	(0, 0, 1, 0, 0, 1, 0): "1",
	(1, 0, 1, 1, 1, 0, 1): "2", #had a mistake (segments 5-6 inverted)
	(1, 0, 1, 1, 0, 1, 1): "3",
	(0, 1, 1, 1, 0, 1, 0): "4",
	(1, 1, 0, 1, 0, 1, 1): "5",
	(1, 1, 0, 1, 1, 1, 1): "6",
	(1, 0, 1, 0, 0, 1, 0): "7",
	(1, 1, 1, 1, 1, 1, 1): "8",
	(1, 1, 1, 1, 0, 1, 1): "9"
}

def read_seg(img,pos):
    #Obtain binary value
    bin = []
    Len = int(np.size(pos)/14)
    for (x,y) in pos:
        #For some reason its inverted
        Val = int(img[y][x]==255)
        bin.append(Val)

    bin = np.reshape(bin,(Len,7))

    #Convert binary to 0-9
    out = []
    for n in np.arange(Len):
		#Display 7bit code
        #print(bin[n])
        num = DIGITS_LOOKUP.get(tuple(bin[n]))
		#Display decoded
        #print(num)
        #Error case
        if num is not None:
            out.append(num)
        else:
            print('Incorrect placement of the segments caused an error, stopping because data is incorrect')
            break
    return out
"""
        #Enable this for trouble shooting
        print('shape: ',np.size(img,0),'by',np.size(img,1))
        print('Position',(x,y))
        if Val == 1:
            print('White')
            cv2.circle(img, (x,y), 5 ,(0, 0, 0), 2)
        else:
            print('Black')
            cv2.circle(img, (x,y), 5 ,(255, 255, 255), 2)
        cv2.imshow('1',img)
        cv2.waitKey(0)
"""
