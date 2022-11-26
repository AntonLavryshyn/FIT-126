def function(x):
    return 3 * x**4 - 4 * x**3 + x**2 - 2 * x - 5

for iteration in range(-10,10):
    num = function(iteration)
    if num < 0:
        a1 = iteration - 1
        b1 = iteration
        beginning = iteration
        break
    # print(iteration, num)

for itt in range(beginning, 10):
    num = function(itt)
    # print(itt ,num)
    if num > 0:
        a2 = itt - 1
        b2 = itt
        break

# print('x1 ∈ [', a1, ';', b1, ']')
# print('x2 ∈ [', a2, ';', b2, ']')

