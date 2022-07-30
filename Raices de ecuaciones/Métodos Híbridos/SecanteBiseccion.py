import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
  return x**5 - 100*x**4 + 3995*x**3 - 79700*x**2 + 794004*x - 3160080
  #return (-1)*0.5*x**2 + 2.5*x + 4.5

def Secante(x0, x1):
  if (f(x1) != f(x0)):
    x2 = x1 - f(x1)*((x1 - x0)/(f(x1) - f(x0)))
    x0 = x1
    x1 = x2
  return x0, x1

def Verificar(a, b, c):
  p = min(b, c)
  q = max(b, c)
  x0 = a
  x1 = b
  df = f(x1) - f(x0)
  pf = -f(x1) * (x1 - x0)
  con1 = df > 0 and ((p - x1) * df) < pf and pf < ((q - x1) * df)
  con2 = df < 0 and ((p - x1) * df) > pf and pf > ((q - x1) * df)
  return con1 or con2

def SecanteBisección(a, b, tol):
  res = pd.DataFrame(columns = ["a", "b", "c", "f(b)", "Método"])
  c = a
  res.loc[0] = [a, b, c, f(b), ""]
  i = 1
  while (abs(f(b)) > tol):
    if (f(a) * f(b) < 0):
      a, b = Secante(a, b)
      res.loc[i] = [a, b, c, f(b), "Secante 1"]
    else:
      if (Verificar(a, b, c)):
        a, b = Secante(a, b)
        res.loc[i] = [a, b, c, f(b), "Secante 2"]
      else:
        b = (b + c) / 2
        res.loc[i] = [a, b, c, f(b), "Bisección"]
    if (f(a) * f(b) < 0):
      c = a
    i += 1
  print(res)
  print("Raíz Aproximada de x =", b)

  xi = np.linspace(-25, 25, 100)
  yi = f(xi)

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.title("Secante - Bisección")
  plt.plot(xi, yi, color="blue", label="Función")
  plt.plot(b, f(b), marker="o", color="red", label="Raíz Aproximada")
  plt.legend()

  plt.show()

a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
tol = float(input("Tolerancia: "))
SecanteBisección(a, b, tol)