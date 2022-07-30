import numpy as np
import pandas as pd

def Jacobi(n, A, b, X):
  error = []
  comp = np.zeros((n))
  resx = np.zeros((n))
  col = []#

  #Lectura de la matriz de coeficientes
  print("Método Jacobi")
  print("Introducir la matriz de coeficientes:")

  for r in range(0, n):
    for c in range(0, n):
      A[(r), (c)] = float(input("Elemento A[" + str(r + 1) + str(c + 1) + "]: "))
    b[(r)] = float(input("b[" + str(r + 1) + "]: "))
    col.append("X" + str(r + 1))#
  tol = float(input("Tolerancia: "))
  res = pd.DataFrame(columns=col)#
  k = 0
  while(True):
    suma = 0
    for r in range(0, n):
      suma = 0
      for c in range(0, n):
        if(c != r):
          suma += A[r, c] * X[c]
      resx[r] = (b[r] - suma)/A[r, r]
    
    del error[:]
    X = resx
    res.loc[k] = X
    k += 1

    #COMPROBACION
    for r in range(0, n):
      suma = 0
      for c in range(0, n):
        suma += A[r, c] * X[c]
      comp[r] = suma
      dif = abs(comp[r] - b[r])
      error.append(dif)
    if(all(i <= tol for i in error)):
      break
  
  print("TABLA DE RESULTADOS")
  print(res)
  print("SOLUCION APROXIMADA")
  for i in range(0, n):
    print("X[", (i + 1), "] =", X[i])

n = int(input("Número de ecuaciones: "))
A = np.zeros((n, n))
b = np.zeros((n))
X = np.zeros((n))
Jacobi(n, A, b, X)