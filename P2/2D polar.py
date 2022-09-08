import numpy as np
import matplotlib.pyplot as plt

#################
## MATEMÁTICAS ##
#################

F0 = 1.75

theta = np.linspace(0, np.pi, 7000000)              #parte a) y b)
#theta = np.linspace(-np.pi/2, np.pi/2, 700000)    #parte c)  


#R = F0 * np.sin(theta)         # parte a)
R = F0 * np.sin(theta)**3     # parte b)
#R = F0 * np.cos(theta)**2 * np.cos(3*theta)**2      #parte c)

k = 0
while R[k] <= 0.707:
    k+=1
print(R[k], theta[k]*180/np.pi)


#################
####  PLOTS  ####
#################

fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(theta,R, 'b', -theta, R, 'b')          #parte a) y b)
#ax.plot(theta,R, 'b')                           #parte c)        
plt.title('Patrón de radiación 2D - sin(θ)^3')

plt.show()

