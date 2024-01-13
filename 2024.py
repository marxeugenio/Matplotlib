import matplotlib.pyplot as plt
import numpy as np

# Criar dados de exemplo
x = np.linspace(0, 10, 100)  # Gera 100 pontos entre 0 e 10
y = np.sin(x)  # Calcula o seno de cada ponto

# Criar o gráfico
plt.plot(x, y, label='Seno(x)')

# Adicionar rótulos e título
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Seno')

# Adicionar uma legenda
plt.legend()

# Exibir o gráfico
plt.show()
