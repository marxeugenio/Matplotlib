import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y, linewidth=2)
plt.scatter(x,y, s=50)
plt.show()