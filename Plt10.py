import matplotlib.pyplot as plt

dias = [1,2,3,4,5,6,7]
visualizações = [500,1000,1500,2000,2500,3000,3500]

plt.plot(dias, visualizações, marker="o", color="r")
plt.xlabel("Dias")
plt.ylabel("Visualizações")
plt.title("Visualizações de um video")

plt.show()