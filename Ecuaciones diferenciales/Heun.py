import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(t, y):
  return np.cos(2 * t) + np.sin(3 * t)
	
def Heun(x, y, xa, n):
  res = pd.DataFrame(columns=['x', 'y', 'k1', 'k2', 'h'])
  k1 = 0
  k2 = 0
  h = abs((x - xa)/n)
  res.loc[0] = [x, y, k1, k2, h]
  for i in range(n):
    k1 = f(x, y)
    k2 = f(x + h, y + (k1 * h))
    y = y + (h/2) * (k1 + k2)
    x = x + h
    res.loc[i + 1] = [x, y, k1, k2, '']
  print(res)

  xi = res.iloc[:, 0].to_numpy()
  yi = res.iloc[:, 1].to_numpy()

  plt.axhline(0, color='black')
  plt.axvline(0, color='black')
  plt.title("Método de Heun")
  plt.plot(xi, yi, label='Función', color='blue')
  plt.legend()
  plt.show()

x = float(input("Ingrese el valor inicial de x: "))
y = float(input("Ingrese el valor inicial de y: "))
xa = float(input("Ingrese el valor auxiliar de x: "))
n = int(input("Ingrese el nro de intervalos: "))
Heun(x, y, xa, n)

#PVI -> y(0) = 1
#aprox y(1) = 2.11148057886752