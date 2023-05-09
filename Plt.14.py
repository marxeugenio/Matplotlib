import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# criando um array de dados aleatórios
data = np.random.randn(10, 10)

# plotando o gráfico de calor com valores numéricos
ax = sns.heatmap(data, cmap='coolwarm', annot=True, fmt='.2f')

# adicionando rótulos de eixo e título
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('Título do Gráfico')

# exibindo o gráfico
plt.show()
