import numpy as np
import matplotlib.pyplot as plt

# Gerando dados aleatórios
x = np.random.normal(size=100)
y = np.random.normal(size=100)

# Plotando o scatter plot
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot de valores aleatórios')
plt.show()
