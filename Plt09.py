import matplotlib.pyplot as plt

produtos = ["Produto A", "Produto B"]
vendas = [100, 75]

cores = ["#ff7f0e","#1f77b4"]

plt.bar(produtos,vendas,color=cores)
plt.xlabel("Produtos")
plt.ylabel("Número de Vendas")
plt.title("Vendas de Produtos em Janeiro")

for i, v in enumerate(vendas):
    plt.text(i, v+3, str(v), color="black", ha="center")

plt.show()