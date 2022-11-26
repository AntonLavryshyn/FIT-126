import math

x1 = round(math.sqrt(int(input('x1:'))), 1)
x2 = float(input('x2:'))
x1_1 = float(input('x1_1:'))
x2_2 = float(input('x2_2:'))

def function(x1, x2, x1_1, x2_2):
    dx1 = abs(x1 - x1_1)/x1
    dx2 = abs(x2 - x2_2)/x2
    print('Перша рівність:', dx1)
    print('Друга рівність:', dx2)

    if (dx1 > dx2):
        print('Друга рівність точніша')
        print(dx1, '>', dx2)
    else:
        print('Перша рівність точніша')
        print(dx2, '<', dx1)


function(x1, x2, x1_1, x2_2)


