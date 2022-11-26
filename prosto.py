def f(x):
    return 3 * pow(x, 4) - 4 * pow(x, 3) + pow(x, 2) - 2 * x - 5

for iteration in range(-10,10):
    num = f(iteration)
    #print(iteration, num)
    if num < 0:
        a1 = iteration - 1
        b1 = iteration
        beginning = iteration
        break

for itt in range(beginning, 10):
    num = f(itt)
    #print(itt, num)
    if num > 0:
        a2 = itt - 1
        b2 = itt
        break

#print('x1 ∈ [', a1, ';', b1, ']')
#print('x2 ∈ [', a2, ';', b2, ']')
eps = 0.001

