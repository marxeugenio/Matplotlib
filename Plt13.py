import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35

# Plotando gráfico de barras agrupados
fig, ax = plt.subplots()
ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women')

# Adicionando rótulos e legendas
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

# Exibindo o gráfico
plt.show()
