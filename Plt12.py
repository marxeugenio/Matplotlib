import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = np.random.rand(10,10)
fig, ax = plt.subplots()
im = ax.imshow(data)
cbar = ax.figure.colorbar(im, ax=ax)
ax.set_xticks(np.arange(data.shape[1]))
ax.set_yticks(np.arange(data.shape[0]))
ax.set_xticklabels(["A","B","C","D","E","F","G","H","I","J"])
ax.set_yticklabels(["1","2","3","4","5","6","7","8","9","10"])
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
ax.set_title("Heatmap example")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_title("Gráfico de Calor")

plt.show()