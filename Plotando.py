import matplotlib.pyplot as plt
import numpy as np

# Dados para o gráfico de pizza
categorias = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D', 'Categoria E']
valores = [15, 30, 25, 10, 20]

# Cores para cada fatia do gráfico
cores = plt.cm.Paired(np.arange(len(categorias)))

# Destacar uma fatia (Categoria B, no índice 1)
explode = (0, 0.1, 0, 0, 0)

# Criar o gráfico de pizza
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(valores, explode=explode, labels=categorias, autopct='%1.1f%%',
                                  shadow=True, startangle=90, colors=cores, wedgeprops=dict(width=0.3))

# Adicionar uma legenda
ax.legend(wedges, categorias, title='Categorias', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))

# Adicionar rótulos personalizados dentro das fatias
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(categorias[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

# Adicionar um título
plt.title('Gráfico de Pizza')

# Mostrar o gráfico
plt.show()
