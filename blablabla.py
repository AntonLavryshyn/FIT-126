from random import randint as rn

m = int(input('Enter m value: '))
n = int(input('Enter n value: '))


def matrix(m, n):
    matrix_zero = [[0] * n for i in range(m)]
    average = 0
    min = 0

    for i in range(m):
        for j in range(n):
            matrix_zero[i][j] = rn(-9, 9)
            average += matrix_zero[i][j] / n
        print('averarage value in', i+1, 'ROW: ', average)

        min = average

        if average > min:
            min = average
    print('the minimum value among the average values: ', min)

    for el in matrix_zero:
        print(el)


matrix(m, n)








