import matplotlib.pyplot as plt

produtos = ["Produtos A", "Produtos B"]
vendas = [100, 75]

plt.bar(produtos, vendas)
plt.xlabel("Produtos")
plt.ylabel("Número de Vendas")
plt.title("Vendas de Produtos em Janeiro")

plt.show()