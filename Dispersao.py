import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Criando dados de exemplo
np.random.seed(0)
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)
colors = np.random.rand(num_points)
sizes = 1000 * np.random.rand(num_points)

# Criando uma figura e um subplot tridimensional
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotando os pontos em um gráfico de dispersão tridimensional
scatter = ax.scatter(x, y, z, c=colors, s=sizes, alpha=0.6)

# Adicionando rótulos e título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gráfico de Dispersão 3D')

# Adicionando uma barra de cores
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Cores')

# Exibindo o gráfico
plt.show()
