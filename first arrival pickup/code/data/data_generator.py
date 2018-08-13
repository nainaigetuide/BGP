import numpy as np
from numpy import sin, sign
from matplotlib import pyplot as plt

m, T = 100, 3000
i = np.tile(np.linspace(1,m,m),(int(T/10),1))
t = np.tile(np.linspace(1,T,int(T/10)),(m,1)).transpose()

# print(i,'\n')
# print(t)
A = 5*np.random.standard_normal([int(T/10),m])*np.exp(-0.001*i)
w = 0.8
beta = 0.5
Y = A*sin(w*(t-np.square(i)*beta))*(1+sign(t-np.square(i)*beta))+1.3*np.random.standard_normal([int(T/10),m])
plt.scatter(i,-t,Y)
t_temp = 1+sign(t-np.square(i)*beta)
t_first = np.zeros([m])
for j in range(m):
    try:
        t_first[j] = np.argwhere(t_temp[:,j])[0]*10
    except:
        t_first[j] = None
# plt.scatter(np.arange(1,m+1),-t_first,c='r',s=2)
plt.figure()
plt.plot(t[:,24],Y[:,24])
plt.show()