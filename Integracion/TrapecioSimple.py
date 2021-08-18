import numpy as np

def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
def TrapecioSimple(a, b):
  A = (b - a) * (f(a) + f(b))/2
  print("Área aproximada de la integrar:", A)

a = float(input("Ingrese limite inferior: "))
b = float(input("Ingrese limite superior: "))
TrapecioSimple(a, b)