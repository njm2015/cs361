from dtw import dtw
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
x = [0,0,1,1,2,2,3,3,0,0,0,1,1,2,2,3,0,0,0,1,1,2,2,3]
y = [0,0,1,1,2,2,3,3]
a = [5,1,2,2,6,6,2,2]
dist, cost, acc, path = dtw(x, a, dist=lambda x,y: (x-y)**2)
print(dist)
print(cost)
print(acc)
print(path)
'''
fig = plt.figure(1)
ax = fig.add_subplot(111)
plot1 = plt.imshow(cost.T, origin='lower', cmap=cm.gray, interpolation='nearest')
plot2 = plt.plot(path[0], path[1], 'w')
xlim = ax.set_xlim((-0.5, cost.shape[0]-0.5))
ylim = ax.set_ylim((-0.5, cost.shape[1]-0.5))
plt.show()
'''