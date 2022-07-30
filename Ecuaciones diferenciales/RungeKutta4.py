import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(t, y):
  return np.cos(2 * t) + np.sin(3 * t)

def RungeKutta4(x, y, xa, n):
  res = pd.DataFrame(columns=['x', 'y', 'k1', 'k2', 'k3', 'k4', 'h'])
  k1 = 0
  k2 = 0
  k3 = 0
  k4 = 0
  h = abs((x - xa)/n)
  res.loc[0] = [x, y, k1, k2, k3, k4, h]
  for i in range(n):
    k1 = f(x, y)
    k2 = f(x + h/2, y + (h/2)*k1)
    k3 = f(x + h/2, y + (h/2)*k2)
    k4 = f(x + h, y + (k3*h))
    y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    x = x + h
    res.loc[i + 1] = [x, y, k1, k2, k3, k4, '']
  print(res)

  xi = res.iloc[:, 0].to_numpy()
  yi = res.iloc[:, 1].to_numpy()

  plt.axhline(0, color='black')
  plt.axvline(0, color='black')
  plt.title("Método de Runge Kutta 4to Orden")
  plt.plot(xi, yi, label='Función', color='blue')
  plt.legend()
  plt.show()

x = float(input("Ingrese el valor inicial de x: "))
y = float(input("Ingrese el valor inicial de y: "))
xa = float(input("Ingrese el valor auxiliar de x: "))
n = int(input("Ingrese el nro de intervalos: "))
RungeKutta4(x, y, xa, n)

#PVI -> y(0) = 1
#aprox y(1) = 2.118013779018466