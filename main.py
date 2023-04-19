import matplotlib.pylab as plt

theta = plt.linspace(0, 10*plt.pi, 500*5) # angle
r = (plt.sin(2.3*theta))**2 + (plt.cos(2.3*theta))**4
plt.polar(theta, r, color='g')
plt.title('graph of sin(2.3x)^2+cos(2,3x)^4 for x in [0, 10pi]', color='r')
plt.show()