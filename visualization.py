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

x_coordinates=np.array([])
y_coordinates=np.array([])
z_coordinates=np.array([])
with open("data.csv") as datafile:
    for line in datafile:
        if line=="\n":
            continue
        data=line.strip().split(",")

        # csv format:
    
        x=float(data[0])
        y=float(data[1])
        z=float(data[2])



        print(x,y,z)
        x_coordinates=np.append(x_coordinates,x)
        y_coordinates=np.append(y_coordinates,y)
        z_coordinates=np.append(z_coordinates,z)

print(x_coordinates,y_coordinates,z_coordinates)
ax.scatter(xs=x,ys=y,zs=z,c="red")

plt.show()
