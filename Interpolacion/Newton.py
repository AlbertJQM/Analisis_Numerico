import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import pandas as pd

def Newton(xi, fi, p):
  #PROCEDIMIENTO
  #Tabla de Diferencias Divididas

  titulo = ['i', 'xi', 'fi']
  n = len(xi)
  ki = np.arange(0, n, 1)
  tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
  tabla = np.transpose(tabla)

  #diferencias divididas vacia
  dfinita = np.zeros(shape=(n, n), dtype=float)
  tabla = np.concatenate((tabla, dfinita), axis=1)

  #Calculo de la tabla, inicia en columna 3
  [n, m] = np.shape(tabla)
  diagonal = n - 1
  j = 3
  while(j < m):
    titulo.append('b[' + str(j - 2) + ']')
    i = 0
    paso = j - 2
    while(i < diagonal):
      denominador = (xi[i + paso] - xi[i])
      numerador = tabla[i + 1, j - 1] - tabla[i, j - 1]
      tabla[i, j] = numerador / denominador
      i = i + 1
    diagonal =  diagonal - 1
    j = j + 1
  
  #Polinomio con diferencias divididas
  dDividida = tabla[0, 3:]
  n = len(dfinita)

  x = sym.Symbol('x')
  polinomio = fi[0]

  for j in range(1, n, 1):
    factor = dDividida[j - 1]
    termino = 1
    for k in range(0, j, 1):
      termino = termino * (x - xi[k])
    polinomio = polinomio + termino * factor
  
  #Simplificando el polinomio
  polsimple = polinomio.expand()

  #Polinomio para evaluaciones
  px = sym.lambdify(x, polsimple)

  #Resultados
  muestras = 100
  a = np.min(xi)
  b = np.max(xi)
  pxi = np.linspace(a, b, muestras)
  pfi = px(pxi)

  res = pd.DataFrame(tabla, columns = [titulo])
  np.set_printoptions(precision = 4)

  print('TABLA DE DIFERENCIAS DIVIDIDAS')
  print(res)
  print('D. Divididas:', dDividida)
  print('Polinomio:', polinomio)
  print('Polinomio simplificado:', polsimple)

  print('Interpolación cuando x =', p, ':', px(p))
  print('Valor real de x =', p, ':', np.sin(np.radians(p)))#

  xr = np.linspace(0, 360, 361)#
  yr = np.sin(np.radians(xr))#

  #Grafica
  plt.axhline(0, color='black')
  plt.axvline(0, color='black')
  plt.xlabel('xi')
  plt.ylabel('fi')
  plt.title('Diferencias Divididas - Newton')
  plt.plot(xr, yr, label='Función Seno', color='yellow')#
  plt.plot(pxi, pfi, label='Polinomio Interpolado', color='blue')
  plt.legend()
  plt.show()

xi = input("Vector x: ")
fi = input("Vector y: ")
p = float(input("Valor a interpolar: "))
xi = np.array(xi.split(','), dtype=float)
fi = np.array(fi.split(','), dtype=float)
Newton(xi, fi, p)
# X -> 60,65,70,75,80
# Y -> 0.866025,0.906308,0.939693,0.965926,0.984808