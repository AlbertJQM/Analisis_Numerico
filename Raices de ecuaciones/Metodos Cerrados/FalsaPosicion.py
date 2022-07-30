import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
  return x ** 3 - 6 * x + 1

def FalsaPosicion(a, b, tol):
  res = pd.DataFrame(columns=['a', 'b', 'm', 'f(a)', 'f(b)', 'f(m)'])
  i = 0
  while(True):
    m = b - ((f(b) * (a - b)) / (f(a) - f(b)))
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
  plt.title('Falsa Posición')
  plt.plot(x, y, color="blue", label='Función')
  plt.plot(m, f(m), color="red", marker='o', label='Raíz Aproximada')
  plt.xlim(-10, 10)
  plt.ylim(-10, 10)
  plt.legend()
  
  plt.show()

FalsaPosicion(a=2, b=3, tol=0.00005)