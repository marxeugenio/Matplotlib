import numpy as np
import matplotlib.pyplot as plt

# Gerando dados Aleatórios

x = np.linspace(0, 10, 100)
y = np.sin(x)

# plotando o gráfico

plt.plot(x,y)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Grafico de uma função senoidal")

plt.show()