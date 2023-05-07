import numpy as np
import matplotlib.pyplot as plt

dados = np.random.normal(size=1000)

plt.hist(dados, bins=30)
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.title("Histograma de Valores")
plt.show()
