import matplotlib.pyplot as plt

# Dados para o gráfico de pizza
labels = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
sizes = [25, 30, 20, 25]  # Porcentagens para cada categoria

# Cores para cada fatia do gráfico
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

# Destacar uma fatia (opcional)
explode = (0.1, 0, 0, 0)

# Criar o gráfico de pizza
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Adicionar um título
plt.title('Gráfico de Pizza')

# Mostrar o gráfico
plt.axis('equal')  # Garante que o gráfico de pizza é desenhado como um círculo.
plt.show()
