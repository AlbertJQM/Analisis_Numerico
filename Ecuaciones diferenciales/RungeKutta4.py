import numpy as np
import pandas as pd

def f(t, y):
    return np.cos(2 * t) + np.sin(3 * t)

def RungeKutta4(x, y, xf, n):
    res = pd.DataFrame(columns = ['#', 'x' , 'y', 'k1', 'k2', 'k3', 'k4', 'h'])
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    h = (xf - x)/n
    res.loc[0]=[0, x, y, k1, k2, k3, k4, h]
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + (1./2)*h, y + (1./2)*(k1 * h))
        k3 = f(x + (1./2)*h, y + (1./2)*(k2 * h))
        k4 = f(x + h, y + (k3 * h))
        y = y + (h/6)*(k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h
        res.loc[i+1]=[i+1, x, y, k1, k2, k3, k4, '']
    print(res)

RungeKutta4(0, 1, 1, 5)

#aprox y(1) = 2.118013779018466