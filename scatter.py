import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


x=np.arange(0,10,1)
plt.scatter(x,x**2,c='red', s=10)
plt.text(3,50, 'y=x^2 graph')
plt.show()