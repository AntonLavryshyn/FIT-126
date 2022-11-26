from scipy import optimize
import math

x0 = 0.95
y0 = 0.975
delta = 0.001


def f1(y):
    return 1.5 - math.cos(y)


def f2(x):
    return 1/2 + math.sin(x + 0.5) / 2


def iteration_method(x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1 - xn) >= e) & (abs(yn1 - yn) >= e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print('Simple iteration:')
    print('x=', round(xn, 5), '\ny=', round(yn, 5), '\nThe amount of iteration = ', n)


iteration_method(x0, y0, delta)


def check_function(x):
    return math.cos(x[1]) + x[0] - 1.5, 2 * x[1] - math.sin(x[0] - 0.5) - 1


optimization = optimize.root(check_function, [0., 0.], method='hybr')
print('Checking...', optimization.x)


