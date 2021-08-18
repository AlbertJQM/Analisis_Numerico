import numpy as np
import pandas as pd

def f(t, y):
    return np.cos(2 * t) + np.sin(3 * t)

def Euler(x, y, xf, n):
    res = pd.DataFrame(columns = ['#', 'x' , 'y', 'h'])
    h = (xf - x)/n
    res.loc[0]=[0, x, y, h]
    for i in range(n):
        y = y + f(x, y) * h
        x = x + h
        res.loc[i+1]=[i+1, x, y, '']
    print(res)
Euler(0, 1, 1, 100)

#aprox y(1) = 2.124289774138598