import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
def Simpson1_3(a, b, n):
  h = (b - a)/n
  sp = 0
  si = 0

  x = np.linspace(a, b, n + 1) #Vector X
  y = f(x) #Vector Y

  for i in range(1, n):
      if(i % 2 == 0):
          sp += y[i]
      else:
          si += y[i]
          
  A = (h / 3) * (y[0] + y[n] + 2 * sp + 4 * si)
  df = pd.DataFrame(list(zip(x, y)), columns = ['x','y'])

  print(df)
  print("Área aproximada de la integrar:", A)

  xi = np.linspace(a, b, 51)
  yi = f(xi)

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.plot(x, y, label='Trapecios', color='red')
  plt.plot(x, y, 'o', label='Puntos', color='blue')
  plt.plot(xi, yi, label='Integral', color='black')
  plt.legend()
  plt.show()

a = float(input("Ingrese limite inferior: "))
b = float(input("Ingrese limite superior: "))
n = int(input("Número de intervalos: "))

Simpson1_3(a, b, n)