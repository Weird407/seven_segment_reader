import numpy as np
import pandas as pd
from numpy import pi
import matplotlib.pyplot as plt
"""
# add the tesseract exe to path
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
"""
mydata= pd.read_csv("test2.csv",header = None, names = ['Temp'])
data = mydata.Temp

#acceptance of difference to remove errors
accept = 0.1
Temperature = []
target = 100

for n in np.arange(np.size(data)):
    if n != 0 and n!=np.size(data)-1:
        if (1-accept)*data[n-1]<data[n]<(1+accept)*data[n+1]:
            Temperature.append(data[n])

#time
Delta = 1
time = Delta*np.arange(np.size(Temperature))/60

#PID terms
rise_min = 0.1*target
rise_max = 0.9*target
RT = []
for t in np.arange(np.size(Temperature)):
    if Temperature[t] > rise_min and Temperature[t]<rise_max:
        RT.append(t)
rise_time = (min(RT),max(RT))

peak = max(Temperature)
peaktime = Temperature.index(peak)
#settlingmin = min(Temperature[Temperature.index(peak):-1])

str = "target: {} c \nrise time: {} sec \npeak: {} c \npeak time: {} sec".format(target, rise_time, peak, peaktime)

plt.plot(time,Temperature)
plt.plot([0,max(time)],[target,target],linestyle='dashed')
plt.xlabel('time [min]')
plt.ylabel('Temperature [c]')
plt.xlim(xmin=0,xmax=max(time))
plt.text(5,30,str, fontsize=12)
plt.show()
