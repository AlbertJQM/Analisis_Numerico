import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
  return ((9.8 * 68.1) / x) * (1 - np.exp((-x / 68.1) * 10)) - 40

x = np.linspace(1, 20, 100)
y = f(x)

x2 = np.linspace(4, 20, 5)
y2 = f(x2)

plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.title('Gráfico')
plt.plot(x, y, color="blue", label='Función')
plt.plot(x2, [0 for i in range(len(x2))], 'o', color="red", label='Puntos')
plt.legend()

plt.show()

df = pd.DataFrame(list(zip(x2, y2)), columns=['c', 'f(c)'])
print(df)

df2 = pd.DataFrame(list(zip(x, y)), columns=['c', 'f(c)'])
print(df2)