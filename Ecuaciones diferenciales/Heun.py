import numpy as np
import pandas as pd

def f(t, y):
    return np.cos(2 * t) + np.sin(3 * t)

def Heun(x, y, xf, n):
    res = pd.DataFrame(columns = ['#', 'x' , 'y', 'k1', 'k2', 'h'])
    k1 = 0
    k2 = 0
    h = (xf - x)/n
    res.loc[0]=[0, x, y, k1, k2, h]
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + (k1 * h))
        y = y + (h/2)*(k1 + k2)
        x = x + h
        res.loc[i+1]=[i+1, x, y, k1, k2, '']
    print(res)
Heun(0, 1, 1, 10)

#aprox y(1) = 2.11148057886752