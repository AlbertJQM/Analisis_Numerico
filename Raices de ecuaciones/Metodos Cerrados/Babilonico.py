import math
import pandas as pd

def Babilonico(P, tol):
    res = pd.DataFrame(columns = ['#', 'x' , 'Error'])
    x = P
    i = 0 
    while(True):
        x0 = x
        x = (x0 + P/x0)/2
        E = abs((x - x0)/x0)
        res.loc[i]=[i, x, E]
        i += 1
        if(E < tol):
            break
    print(res)
    print("Aproximacion de la raiz cuadrada de",P,"es:",x)
    print("Valor real:", math.sqrt(P))

P = float(input("Raiz a calcular: "))
Babilonico(P, tol=0.00001)