import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def Newton(xi, fi):
  # PROCEDIMIENTO

  # Tabla de Diferencias Divididas Avanzadas
  titulo = ['i   ','xi  ','fi  ']
  n = len(xi)
  ki = np.arange(0,n,1)
  tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
  tabla = np.transpose(tabla)

  # diferencias divididas vacia
  dfinita = np.zeros(shape=(n,n),dtype=float)
  tabla = np.concatenate((tabla,dfinita), axis=1)

  # Calcula tabla, inicia en columna 3
  [n,m] = np.shape(tabla)
  diagonal = n-1
  j = 3
  while (j < m):
      # Añade título para cada columna
      titulo.append('F['+str(j-2)+']')

      # cada fila de columna
      i = 0
      paso = j-2 # inicia en 1
      while (i < diagonal):
          denominador = (xi[i+paso]-xi[i])
          numerador = tabla[i+1,j-1]-tabla[i,j-1]
          tabla[i,j] = numerador/denominador
          i = i+1
      diagonal = diagonal - 1
      j = j+1

  # POLINOMIO con diferencias Divididas
  # caso: puntos equidistantes en eje x
  dDividida = tabla[0,3:]
  n = len(dfinita)

  # expresión del polinomio con Sympy
  x = sym.Symbol('x')
  polinomio = fi[0]
  for j in range(1,n,1):
      factor = dDividida[j-1]
      termino = 1
      for k in range(0,j,1):
          termino = termino*(x-xi[k])
      polinomio = polinomio + termino*factor

  # simplifica multiplicando entre (x-xi)
  polisimple = polinomio.expand()

  # polinomio para evaluacion numérica
  px = sym.lambdify(x,polisimple)

  # Puntos para la gráfica
  muestras = 101
  a = np.min(xi)
  b = np.max(xi)
  pxi = np.linspace(a,b,muestras)
  pfi = px(pxi)

  # SALIDA
  np.set_printoptions(precision = 4)
  print('Tabla Diferencia Dividida')
  print([titulo])
  print(tabla)
  print('D. Dividida:', dDividida)
  print('Polinomio:', polinomio)
  print('Polinomio simplificado:', polisimple)

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
  plt.ylabel('fi')
  plt.title('Diferencias Divididas - Newton')
  plt.show()

# INGRESO , Datos de prueba
xi = np.array([60,65,70,75,80])
fi = np.array([0.866025,0.906308,0.939693,0.965926,0.984808])

Newton(xi, fi)