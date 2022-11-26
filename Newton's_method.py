import math
import numpy as np
from scipy.misc import derivative
from prosto import f, a1, b1, a2, b2, eps

a1 = a1
b1 = b1
a2 = a2
b2 = b2
eps = eps

def nuton(a, b, eps):
    df2 = derivative(f, b, n=2)
    if f(b) * df2 > 0:
        xi = b
    else:
        xi = a
    df = derivative(f, xi, n=1)
    xi_1 = xi - f(xi) / df
    while (abs(xi_1 - xi) > eps):
        xi = xi_1
        xi_1 = xi - f(xi) / df
    return print('Solving the equation by Newton8s method x =', round(xi_1, 5))

nuton(a1, b1, eps)
nuton(a2, b2, eps)


