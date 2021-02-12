import numpy as np
import pandas as pd
from scipy import interpolate
import matplotlib.pyplot as plt

numdat = pd.read_excel('C:\\Users\\pc\\.spyder-py3\\openCV\\TimeSeries.xlsx')

numdat_1 = numdat[0:149]
num1=np.array(numdat_1)

numdat_2=[]*149
for k in range(0,len(num1)-99):
    value=3*k+1
    print(value)
    numdat_2.append(num1[value])

plt.plot(num1,numdat_2, marker="o", ls="")
sx=np.log10(num1)
xi_ = np.linspace(sx.min(),sx.max(), num=201)
xi = 10**(xi_)

f = interpolate(sx,numdat_2, kind="cubic")
yi = f(xi_)
plt.plot(xi,yi, label="cubic spline")


f1 = interpolate(sx,numdat_2, kind="line")
yi = f1(xi_)
plt.plot(xi,yi, label="line spline")

plt.gca().set_xscale("log")
plt.legend()
plt.show()






