import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,np.pi*2,100)
print(plt.style.available)
plt.style.use('seaborn-v0_8')
plt.plot(x,np.sin(x), 'r-', label="sin_curve")
plt.plot(x, np.cos(x),'b-',label="cos curve")
plt.xlabel("x value")
plt.ylabel("y value")
plt.legend()
plt.show()