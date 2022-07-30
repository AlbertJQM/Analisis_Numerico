import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sympy as sp
import math

def Secante(f, x0, xi, tol):
  x = sp.Symbol('x')
  f = sp.sympify(f)
  res = pd.DataFrame(columns=['x', 'f(x)'])
  F0 = f.evalf(subs={x:x0})
  F1 = f.evalf(subs={x:xi})
  res.loc[0] = [x0, F0]
  res.loc[1] = [xi, F1]
  i = 2
  while(abs(f.evalf(subs={x:xi})) > tol):
    x1 = xi
    F0 = f.evalf(subs={x:x0})
    F1 = f.evalf(subs={x:x1})
    xi = x1 - ((F1 * (x0 - x1))/(F0 - F1))
    F = f.evalf(subs={x:xi})
    res.loc[i] = [xi, F]
    i += 1
    x0 = x1
  print(res)
  print("Raiz aproximada de x = ", xi)

  x_i = np.linspace(-5, 5, 100)
  y_i = np.array([f.evalf(subs={x:x_i[i]}) for i in range(len(x_i))])

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.title("Secante")
  plt.plot(x_i, y_i, color="blue", label="Función")
  plt.plot(xi, f.evalf(subs={x:xi}), marker='o', color="red", label="Raíz Aproximada")
  plt.legend()

  plt.show()

f = input("Función f(x): ")
x1 = float(input("Valor de x1: "))
x2 = float(input("Valor de x2: "))
tol = float(input("Tolerancia: "))
Secante(f, x1, x2, tol)