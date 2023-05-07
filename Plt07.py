import matplotlib.pyplot as plt
import numpy as np

# Dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Criando o gráfico
plt.plot(x, y)

# Definindo limites dos eixos x e y
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# Definindo escala do eixo y
plt.yscale('linear')  # 'linear' é a escala padrão
# plt.yscale('log')  # escala logarítmica

# Exibindo o gráfico
plt.show()
