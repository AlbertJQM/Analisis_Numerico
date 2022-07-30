import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
  return 0.2 * np.sin(16 * x) - x + 1.75
  #return -0.5*x**2 + 2.5*x + 4.5

def df(x):
  return 3.2 * np.cos(16 * x) - 1
  #return 2.5 - x

def NewtonBisección(a, b, tol):
  res = pd.DataFrame(columns = ["a", "b", "x", "f(x)", "Método"])
  x = a
  i = 0
  res.loc[i] = [a, b, x, f(x), ""]
  while (abs(f(x)) > tol):
    i += 1
    con1 = (df(x) > 0 and (a - x)*df(x) < -f(x) and (b - x)*df(x) > -f(x))
    con2 = (df(x) < 0 and (a - x)*df(x) > -f(x) and (b - x)*df(x) < -f(x))
    if (con1 or con2 or (f(x) == 0)):
      x = x - (f(x)/df(x))
      res.loc[i] = [a, b, x, f(x), "Newton"]
    else:
      x = (a + b)/2
      res.loc[i] = [a, b, x, f(x), "Bisección"]
    if (f(a) * f(x) < 0):
      b = x
    else:
      a = x

  print(res)
  print("Raíz Aproximada de x =", x)
  
  xi = np.linspace(-5, 5, 100)
  yi = f(xi)

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.title("Newton - Bisección")
  plt.plot(xi, yi, color="blue", label="Función")
  plt.plot(x, f(x), marker="o", color="red", label="Raíz Aproximada")
  plt.legend()

  plt.show()


a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
tol = float(input("Tolerancia: "))
NewtonBisección(a, b, tol)