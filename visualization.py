from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time


def normalize(x):
    return (x-x.min())/(x.max()-x.min())
def colour(x):
    return np.exp(-0.02*(x-33)**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.gca()

ax.hold(True)
ax.set_xlim([0,10])
ax.set_ylim([0,10])
ax.set_zlim([0,10])


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x_coordinates=np.array([])
y_coordinates=np.array([])
z_coordinates=np.array([])
colours=np.array([])
with open("cave_final.csv") as datafile:
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
        x_coordinates=np.append(x_coordinates,distance*np.cos(angle)*1)
        y_coordinates=np.append(y_coordinates,y)
        z_coordinates=np.append(z_coordinates,distance*np.sin(angle)*1)
        print(colour(y))
        colours=np.append(colours,colour(y))
colours=normalize(colours)
print(colours)
r=colours*256
g=colours*256
b=colours*256
plt.axis('off')
rgb_colours=np.dstack((r,g,b))
print(rgb_colours)
xx, yy = np.meshgrid(range(-10,20), range(-10,200))
ax.plot_surface(xx,yy,0*xx, alpha=0.2)

#print(x_coordinates,y_coordinates,z_coordinates)
ax.scatter(xs=x_coordinates,ys=y_coordinates,zs=z_coordinates,c=colours)

plt.show()
