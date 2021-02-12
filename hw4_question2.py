import matplotlib.pyplot as plt
from math import e, cos, pi
from PIL import Image, ImageFilter  

ft = []
tVal = []
gt=[]

def f(t):
    return (3*(e *-3*t)*cos(2*pi*t/3))-(5*t*(e*-t))-(2*(e **-t))

def g(t):
    
    if 0 <= t <= 4:
        return f(t)
    else:
        return -f(t)
 
t = 0   
while t <= 10:
    tVal.append(t)
    ft.append(f(t))
    gt.append(g(t))
    t += 0.001

plt.plot(tVal, ft)
plt.show()

plt.plot(tVal, gt)
plt.show()

im1=Image.open('C:\\Users\\pc\\.spyder-py3\\openCV\\f(t).png')
im2=im1.filter(ImageFilter.MedianFilter(size=3))
im2.show()


