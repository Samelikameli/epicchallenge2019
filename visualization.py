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
with open("cave_data.csv") as datafile:
    for line in datafile:
        if line=="\n":
            continue
        data=line.split()
        
        
        print(data)

        # Traversed distance, unit probably cm?
        y=float(data[0])

        # Angle, degrees to radians
        angle=float(data[1])/180*np.pi
        
        # Distance from the ceiling or wall, unit probably cm?
        distance=float(data[2])

        # As a cross section, y is the direction of the movement, z is vertical and x horizontal

        # Use some trigonometry to place points
        print(angle)
        x_coordinates=np.append(x_coordinates,distance*np.cos(angle)*0.1)
        y_coordinates=np.append(y_coordinates,data[0])
        z_coordinates=np.append(z_coordinates,distance*np.sin(angle)*0.1)

#print(x_coordinates,y_coordinates,z_coordinates)
ax.scatter(xs=x_coordinates,ys=y_coordinates,zs=z_coordinates,c="red")

plt.show()
