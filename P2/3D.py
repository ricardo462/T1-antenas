from cmath import sqrt
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

#################
## MATEMÁTICAS ##
#################

F0 = 1

theta, phi = np.linspace(0, np.pi, 100), np.linspace(0, 2* np.pi, 100)
THETA, PHI = np.meshgrid(theta, phi)


#R = F0 * np.sin(THETA)         # parte a)
R = F0 * np.sin(THETA)**3      # parte b)

#R = F0 * np.cos(THETA)**2 * np.cos(3*THETA)**2      #parte c)
#for i in np.arange(len(R)):
#    for j in np.arange(len(R[0])):
#        if THETA[i][j] > np.pi/2:
#            R[i][j] = 0


X = R * np.sin(THETA) * np.cos(PHI)
Y = R * np.sin(THETA) * np.sin(PHI)
Z = R * np.cos(THETA)








#################
####  PLOTS  ####
#################

fig = plt.figure()
ax = plt.axes(projection='3d')


plt.rcParams["figure.figsize"] = (6, 6)


ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_zlim(-1.1, 1.1)




ax.plot_surface(X, Y, Z, rstride=5, cstride=5,facecolors=cm.coolwarm(R), cmap='coolwarm' )
m = cm.ScalarMappable(cmap=cm.coolwarm)
m.set_array(R)
cbar = fig.colorbar(m,shrink=0.8, aspect=9)
plt.rc('ytick', labelsize=7)






ax.set_title('Patrón de radiación 3D - sin^3(θ)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()