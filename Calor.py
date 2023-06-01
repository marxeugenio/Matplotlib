import matplotlib.pyplot as plt
import numpy as np

# Gerar dados aleatórios
np.random.seed(0)
x = np.random.randn(1000)
y = np.random.randn(1000)

# Plotar os pontos em uma grade de cores
plt.scatter(x, y, c=x+y, cmap='Spectral')

# Configurações adicionais
plt.title('Gráfico De Calor')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.colorbar(label='Soma X + Y')

# Exibir o gráfico
plt.show()
