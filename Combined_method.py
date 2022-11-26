import math
import numpy as np
from scipy.misc import derivative
from prosto import f, a1, b1, a2, b2, eps

a1 = a1
b1 = b1
a2 = a2
b2 = b2
eps = eps

def komb(a, b, eps):
    if (derivative(f, a, n=1) * derivative(f, a, n=2) > 0):
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai-bi) > eps:
        ai_1 = ai - f(ai) * (bi - ai) / (f(bi) - f(ai))
        bi_1 = bi - f(bi) / derivative(f, bi, n=1)
        ai = ai_1
        bi = bi_1
    x = (ai_1 + bi_1) / 2
    return print('Solving the equation by the combined method x = ', round(x, 5))

komb(a1, b1, eps)
komb(a2, b2, eps)

