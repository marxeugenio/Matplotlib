import matplotlib.pyplot as plt

x = ["A","B","C","D","E",]
y1 = [10,20,30,40,50]
y2 = [20,30,10,50,40]

plt.plot(x,y1, label="Série 1")
plt.plot(x,y2, label="Série 2")
plt.title("Gráfico de Linhas")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend("XY")
plt.show()