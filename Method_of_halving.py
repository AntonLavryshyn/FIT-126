
import numpy as np
import matplotlib.pyplot as plt
import Choose_random_variant

def function(x):
    return 3 * x**4 - 4 * x**3 + x**2 - 2 * x - 5

first_root_a = fhewf.a1
first_root_b = fhewf.b1
second_root_a = fhewf.a2
second_root_b = fhewf.b2
eps = 0.001


def rec_dyhotomy(a, b, eps):
    if abs(function(b) - function(a)) < eps:
        print('calculate root: ')
        return
    mid = (a + b) / 2
    if function(mid) == 0 or abs(function(mid)) < eps:
        print('the root is at the poit x = {mid}')
    elif function(a) * function(mid) < 0:
        rec_dyhotomy(a, b, eps)
    else:
        rec_dyhotomy(mid, b, eps)

x1 = np.arange(first_root_a, first_root_b, eps)
x2 = np.arange(second_root_a, second_root_b, eps)


plt.plot(x1, function(x1))
plt.plot(x2, function(x2))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Method of halving')
plt.grid()
plt.show()


