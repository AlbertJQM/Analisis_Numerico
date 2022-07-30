import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

def f(x):
  return x**3 - 6*x + 1

def Biseccion(a, b, tol):
  res = pd.DataFrame(columns=['a', 'b', 'm', 'f(a)', 'f(b)', 'f(m)'])
  i = 0
  while(True):
    m = (a + b) / 2
    res.loc[i] = [a, b, m, f(a), f(b), f(m)]
    i += 1
    if(f(a) * f(m) < 0):
      b = m
    elif(f(m) * f(b) < 0):
      a = m
    else:
      print("Se hallo una Solucion x =", m)
      break
    if(abs(f(m)) < tol):
      break
  print(res)
  print("Raiz aproximada: x =", m)
  #GRÁFICA
  x = np.linspace(-10, 10, 101)
  y = f(x)

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.title('Bisección')
  plt.plot(x, y, color="blue", label='Función')
  plt.plot(m, f(m), color="red", marker='o', label='Raíz Aproximada')
  plt.xlim(-10, 10)
  plt.ylim(-10, 10)
  plt.legend()

  plt.show()

Biseccion(a=2, b=3, tol=0.00005)