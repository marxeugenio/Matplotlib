import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simula dados de uma pesquisa
idade = np.random.normal(35, 10, 500)
renda = np.random.normal(1500, 500, 500)
genero = np.random.normal(["M","F"], 500, p=[0.4, 0.6])

# Cria um dataframe com os dados simulados
data = pd.DataFrame({"idade": idade, "renda": renda, "genero": genero})

# Exibi as 10 primeiras linhas dos dados
print(data.head(10))

# Calcula a média de renda por gênero
media_por_genero = data.grouphy("genero")["renda"].mean()

# Exibi a média de renda por gênero
print(media_por_genero)

# Cria um gráfico de dispersão para idade e renda
plt.scatter(data["idade"], data["renda"])
plt.title("Idade vs Renda")
plt.xlabel("Idade")
plt.ylabel("Renda")
plt.show()

# Cria um gráfico de barras para a média de renda por gênero
plt.bar(media_por_genero.index, media_por_genero.values)
plt.title("Mpedia de Renda por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Média de Renda")
plt.show()