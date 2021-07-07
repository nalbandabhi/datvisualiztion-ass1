sine wave
=============
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline
import seaborn as sns
from numpy.random import randn, randint, uniform, sample
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y,"r",linestyle="dashed",linewidth="5",markersize="5")
plt.title("Sine wave")
plt.xlabel("X axis")
plt.ylabel("Y axis")