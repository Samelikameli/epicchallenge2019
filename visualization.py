from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.gca()


ax.set_xlim([0,10])
ax.set_ylim([0,10])
ax.set_zlim([0,10])


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


with open("data.csv") as datafile:
    for line in datafile:
        if line=="\n":
            continue
        data=line.strip().split(",")
        x=data[0]
        y=data[1]
        z=data[2]


plt.show()
