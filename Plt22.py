import matplotlib.pyplot as plt

# Dados fictícios
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas_produto1 = [100, 120, 90, 80, 110, 70]
vendas_produto2 = [80, 100, 110, 70, 90, 120]

# Configurar o gráfico
plt.figure(figsize=(8, 5))  # Tamanho da figura

# Plotar os dados
plt.plot(meses, vendas_produto1, marker='o', label='Produto 1')
plt.plot(meses, vendas_produto2, marker='o', label='Produto 2')

# Configurar os eixos
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.title('Vendas Mensais')

# Adicionar legenda
plt.legend()

# Mostrar o gráfico
plt.show()
