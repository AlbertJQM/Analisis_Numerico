import numpy as np
import scipy.linalg as la

def LU(n, A, b):
  print("Método LU")
  print("Introducir la matriz de coeficientes:")

  for r in range(0, n):
    for c in range(0, n):
      A[(r), (c)] = float(input("Elemento A[" + str(r + 1) + str(c + 1) + "]: "))
    b[(r)] = float(input("b[" + str(r + 1) + "]: "))
  P, L, U = la.lu(A)
  print("L", L)
  print("U", U)

  invL = np.linalg.inv(L)
  D = invL @ b
  print("D", D)
  
  invU = np.linalg.inv(U)
  X = invU @ D
  print("X", X)

n = int(input("Número de ecuaciones: "))
A = np.zeros((n, n))
b = np.zeros((n))
LU(A, b)