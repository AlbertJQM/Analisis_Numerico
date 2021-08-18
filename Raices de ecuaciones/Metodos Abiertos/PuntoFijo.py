import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

def f(x):
    return np.exp(-x) - x
def g(x):
    return np.exp(-x)
    
def Punto_Fijo(x0, tol):
  res = pd.DataFrame(columns = ['x' , 'Error'])
  i = 0
  x = g(x0)
  while(abs(x - x0) > tol):
      res.loc[i]=[x, abs(x - x0)]     
      i += 1
      x0 = x
      x = g(x0)
  print(res)
  print("Raiz aproximada: x =", x)

  xi = np.linspace(-2, 2, 51)
  yi = f(xi)
  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.plot(xi, yi, color="blue")
  plt.plot(x, f(x), marker="o",color="red")

  plt.show()

Punto_Fijo(x0=0, tol=0.0005)