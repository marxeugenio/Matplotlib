import numpy as np
import matplotlib.pyplot as plt

# Dados para o gráfico de calor
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Plotagem do gráfico de calor
plt.imshow(Z, cmap='coolwarm', extent=[-5, 5, -5, 5])

# Configurações do gráfico
plt.title('Gráfico de Calor')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.colorbar(label='Valores')

# Exibição do gráfico
plt.show()
