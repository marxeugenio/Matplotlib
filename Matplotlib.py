import numpy as np
import matplotlib.pyplot as plt

vetor = np.linspace(0, 2*np.pi, 500)
x = np.cos(4*vetor)

plt.plot(vetor, x)
plt.title('Grafico do Cosseno')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()