import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(t, y):
  return np.cos(2 * t) + np.sin(3 * t)

def Euler(x, y, xa, n):
  res = pd.DataFrame(columns=['x', 'y', 'h'])
  h = abs((x - xa)/n)
  res.loc[0] = [x, y, h]
  for i in range(n):
    y = y + f(x, y) * h
    x = x + h
    res.loc[i + 1] = [x, y, '']

  print(res)
  xi = res.iloc[:, 0].to_numpy()
  yi = res.iloc[:, 1].to_numpy()

  plt.axhline(0, color='black')
  plt.axvline(0, color='black')
  plt.title("Método de Euler")
  plt.plot(xi, yi, label='Función', color='blue')
  plt.legend()
  plt.show()

x = float(input("Ingrese el valor inicial de x: "))
y = float(input("Ingrese el valor inicial de y: "))
xa = float(input("Ingrese el valor auxiliar de x: "))
n = int(input("Ingrese el nro de intervalos: "))
Euler(x, y, xa, n)

s
#aprox y(1) = 2.124289774138598