import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

def f(x):
  return np.exp(-x) - x
def g(x):
  return np.exp(-x)
    
def Punto_Fijo(x0, tol):
  res = pd.DataFrame(columns = ['x', 'g(x)' , 'Error %'])
  res.loc[0]=[x0, f(x0), ""]
  i = 1
  while(True):
      x = g(x0)
      res.loc[i]=[x, g(x), abs(x - x0) * 100]     
      i += 1
      if(abs(x - x0) < tol):
        break
      x0 = x
  print(res)
  print("Raiz aproximada: x =", x)

  xi = np.linspace(-2, 2, 51)
  yi = f(xi)
  yi2 = g(xi)

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.title('Punto Fijo')
  plt.plot(xi, yi, color="blue", label='Función Original')
  plt.plot(xi, yi2, color="green", label='Función Modificada')
  plt.plot(x, f(x), marker="o", color="red", label='Raíz Aproximada')
  plt.legend()

  plt.show()

Punto_Fijo(x0=0, tol=0.00005)