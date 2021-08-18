import numpy as np

def GaussSeidel(n, A, b, X):
    comp = np.zeros((n))
    error = []
    
    print("Metodo Gauss-Seidel")
    print("Introducir la matriz de coeficientes: ")
    for r in range(0, n):
        for c in range(0, n):
            A[(r), (c)] = float(input("Elemento A[" + str(r + 1) + str(c + 1) + "]: "))
        b[(r)] = float(input("b[" + str(r + 1) + "]: "))
    tol = float(input("Tolerancia: "))
    
    print("Solucion con NumPy: ", np.linalg.solve(A, b))
    
    k = 0
    while(True):
        suma = 0
        k += 1
        for r in range(0, n):
            suma = 0
            for c in range(0, n):
                if(c != r):
                    suma += A[r, c] * X[c]
            X[r] = (b[r] - suma)/A[r,r]
        
        del error[:] #vaciar el contenido de la lista
        #Comprobacion
        for r in range(0, n):
            suma = 0
            for c in range(0, n):
                suma += A[r, c] * X[c]
            comp[r] = suma
            dif = abs(comp[r] - b[r])
            error.append(dif)
        if(all(i <= tol for i in error)):
            break
    for i in range(0, n):
        print("X[", (i + 1), "] = ", X[i])

n = int(input("Numero de ecuaciones e incognitas: "))
A = np.zeros((n, n))
X = np.zeros((n))
b = np.zeros((n))
GaussSeidel(n, A, b, X)