import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
data = pd.read_csv("vendas.csv")

# Exibi as 10 primeiras linhas dos dados
print(data.head(10))

# Calcula a média de vendas por ano
media_por_ano = data.groupby("ano")["vendas"].mean()

# Exibi a média de vendas por ano
print(media_por_ano)

# Calcula o total de vendas por categoria
total_por_categoria = data.groupby("categoria")["vendas"].sum()

# Exibi o total de vendas por categoria
print(total_por_categoria)

# Cria um gráfico de barras para o total de vendas por cateogoria
plt.bar(total_por_categoria.index, total_por_categoria.values)
plt.title("Total de Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Total de Vendas")
plt.show()

# Cria um gráfico de linha para a média de vendas por ano
plt.plot(media_por_ano.index, media_por_ano.values)
plt.title("Média de Vendas por Ano")
plt.xlabel("Ano")
plt.ylabel("Média de Vendas")
plt.show() 