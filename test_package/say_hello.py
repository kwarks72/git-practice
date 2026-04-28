import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# x=np.arange(10)
# plt.plot(x**2)
# plt.axis([0,100,0,100])
# plt.show()

# N=50
# x=np.arange(N)
# y=np.random.random(size=N)

# plt.plot(x,y,'g^:')

x=np.linspace(0,np.pi*2,100)
fig=plt.figure()
plt.plot(x, np.sin(x),'r-')
plt.plot(x,np.cos(x), 'b:')
fig.savefig('sin_cos_fig.png')
plt.show()