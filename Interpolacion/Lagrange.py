import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def Lagrange(xi, fi, p):
  n = len(xi)
  x = sym.Symbol('x')

  polinomio = 0
  for i in range(0, n, 1):
    numerador = 1
    denominador = 1
    for j in range(0, n, 1):
      if (j != i):
        numerador = numerador * (x - xi[j])
        denominador = denominador * (xi[i] - xi[j])
    terminoLi = numerador / denominador
    polinomio = polinomio + terminoLi * fi[i]
  
  polsimple = polinomio.expand()

  px = sym.lambdify(x, polsimple)
  
  print("Polinomio: ", polinomio)
  print("Polinomio simplificado: ", polsimple)
  
  #Puntos para la gráfica
  muestras = 100
  a = np.min(xi)
  b = np.max(xi)
  pxi = np.linspace(a,b,muestras)
  pfi = px(pxi)
  
  #Gráfica

  xr = np.linspace(0, 360, 361)#
  yr = np.sin(np.radians(xr))#

  plt.axhline(0, color="black")
  plt.axvline(0, color="black")
  plt.plot(xr, yr, label = 'Funcion Seno', color = 'yellow')#
  plt.plot(pxi, pfi, label = 'Interpolacion', color = 'blue')
  plt.legend()
  plt.xlabel('xi')
  plt.ylabel('fi')
  plt.title('Interpolación de Lagrange')
  
  print("Interpolación cuando x =", p,":", px(p))
  plt.show()

  print("Solución verdadera:", np.sin(np.radians(p)))#

xi = input("Vector x: ")
fi = input("Vector y: ")
xi = np.array(xi.split(','), dtype='float')
fi = np.array(fi.split(','), dtype='float')
p = float(input("Valor a interpolar: "))
Lagrange(xi, fi, p)
#X -> 60,65,70,75,80
#Y -> 0.866025,0.906308,0.939693,0.965926,0.984808