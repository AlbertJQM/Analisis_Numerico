import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

def f(x): 
    return np.exp(-x) - x

def Secante(x0, x, tol):
  res = pd.DataFrame(columns = ['x' , 'f(x)'])
  i = 2
  res.loc[0]=[x0, f(x0)]
  res.loc[1]=[x, f(x)]
  while(abs(f(x)) > tol):
      x1 = x
      x = x1 - (f(x1) * (x0 - x1))/(f(x0) - f(x1))
      res.loc[i]=[x, f(x)]
      i += 1
      x0 = x1
  print(res)
  print("Solucion aproximada de x = ",x)

  xi = np.linspace(-2, 2, 51)
  yi = f(xi)

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.plot(xi, yi, color="blue")
  plt.plot(x, f(x), marker="o",color="red")

  plt.show()

Secante(x0=0, x=0.1, tol=0.0005)