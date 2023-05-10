import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

np.random.seed(42)

x = np.random.rand(10, 2)
Z = linkage(x, 'ward')

fig, ax = plt.subplots(figsize=(15, 10))

dendrogram(Z)

plt.show()