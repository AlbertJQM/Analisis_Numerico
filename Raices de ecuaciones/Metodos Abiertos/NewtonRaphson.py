import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

def f(x): 
  return np.exp(-x) - x

def df(x): 
  return -np.exp(-x) - 1

def NewtonRaphson(x, tol):
  res = pd.DataFrame(columns = ['x' , 'f(x)', "f'(x)"])
  i = 0
  while(abs(f(x)) > tol): 
      res.loc[i]=[x, f(x), df(x)]
      i += 1
      x = x - (f(x)/df(x))
  res.loc[i]=[x, f(x), df(x)]
  print(res)
  print("Raiz aproximada de x = ",x)

  xi = np.linspace(-2, 2, 51)
  yi = f(xi)

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.title('Newton-Raphson')
  plt.plot(xi, yi, color="blue", label='Función')
  plt.plot(x, f(x), marker="o",color="red", label='Raíz Aproximada')
  plt.legend()

  plt.show()

NewtonRaphson(x=0, tol=0.0005)