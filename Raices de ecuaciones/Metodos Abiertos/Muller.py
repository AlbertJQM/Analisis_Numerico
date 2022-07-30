import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp
import math
def Muller(f, x0, x1, tol):
  x = sp.Symbol('x')
  f = sp.sympify(f)
  i = 0
  res = pd.DataFrame(columns=["x0", "x1", "x2", "x", "f(x)"])
  x2 = (x0 + x1) / 2
  while (True):
    h0 = x1 - x0
    h1 = x2 - x1
    delta0 = (f.evalf(subs={x:x1}) - f.evalf(subs={x:x0})) / (x1 - x0)
    delta1 = (f.evalf(subs={x:x2}) - f.evalf(subs={x:x1})) / (x2 - x1)
    a = (delta1 - delta0) / (h1 - h0)
    b = a * h1 + delta1
    c = f.evalf(subs={x:x2})
    if (b > 0):
      xi = x2 + ((-2 * c) / (b + math.sqrt(b**2 - 4 * a * c)))
    else:
      xi = x2 + ((-2 * c) / (b - math.sqrt(b**2 - 4 * a * c)))
    res.loc[i] = [x0, x1, x2, xi, f.evalf(subs={x:xi})]
    i += 1
    x0 = x1
    x1 = x2
    x2 = xi
    if (abs(f.evalf(subs={x:xi})) < tol): # o se puede utilizar la siguiente variante -> abs((x2 - x1) / x2) < tol
      break
  print(res)
  print("Raíz Aproximada de x =", xi)
  
  x_i = np.linspace(-5, 5, 100)
  y_i = np.array([f.evalf(subs={x:x_i[i]}) for i in range(len(x_i))])
  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.title("Muller")
  plt.plot(x_i, y_i, color="blue", label="Función")
  plt.plot(xi, f.evalf(subs={x:xi}), marker='o', color="red", label="Raíz Aproximada")
  plt.legend()

  plt.show()

f = input("Función f(x): ")
x0 = float(input("Valor de x0: "))
x1 = float(input("Valor de x1: "))
tol = float(input("Tolerancia: "))
Muller(f, x0, x1, tol)