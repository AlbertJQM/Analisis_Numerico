import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def Lagrange(xi, fi):
  #Polinomio de Lagrange
  n = len(xi)
  x = sym.Symbol('x')

  polinomio = 0
  divisorL = np.zeros(n, dtype = float)
  for i in range(0, n, 1):
      #Terminos de Lagrange
      numerador = 1
      denominador = 1
      for j in range(0, n, 1):
          if(j != i):
              numerador = numerador * (x - xi[j])
              denominador = denominador * (xi[i] - xi[j])
      terminoLi = numerador/denominador
      polinomio = polinomio + terminoLi * fi[i]
      divisorL[i] = denominador

  #Simplifica polinomio
  polisimple = polinomio.expand()

  #Para la evaluacion numerica
  px = sym.lambdify(x, polisimple)

  #Puntos de la grafica
  muestras = 101
  a = np.min(xi)
  b = np.max(xi)
  pxi = np.linspace(a, b, muestras)
  pfi = px(pxi)

  print("Valores de x: ", xi)
  print("Imagenes de x: ", fi)
  print("Divisores en L(i):", divisorL)

  print("Polinomio: ", polinomio)
  print("Polinomio Simplificado: ", polisimple)

  print("Interpolacion cuando x = 66: ", px(66))
  print("Solución verdadera:", np.sin(np.radians(66)))

  xr = np.linspace(0, 360, 361)
  yr = np.sin(np.radians(xr))

  # Gráfica
  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.plot(xr, yr, label = 'Funcion Seno', color = 'yellow')
  plt.plot(pxi,pfi, label = 'Polinomio', color = 'blue')
  plt.legend()
  plt.xlabel('xi')
  plt.ylabel('yi')
  plt.title('Interpolacio de Lagrange')
  plt.show()

xi = np.array([60,65,70,75,80])
fi = np.array([0.866025,0.906308,0.939693,0.965926,0.984808])

Lagrange(xi, fi)