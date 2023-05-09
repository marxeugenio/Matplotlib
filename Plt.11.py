import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()
x = np.random.normal(size=100)
y = 2 * x + np.random.normal(size=100)

x_mean = np.mean(x)
y_mean = np.mean(y)

slope = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
intercept = y_mean - slope * x_mean
line = slope * x + intercept


plt.scatter(x,y)
plt.plot(x,line, color="red",linewidth=3)
plt.title("Gráfico de Regressão Linear")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("plt.png")
plt.show()