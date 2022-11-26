from math import factorial
import matplotlib.pyplot as plt
import numpy as np

x = [0.180, 0.185, 0.190, 0.195, 0.2, 0.205, 0.210, 0.215, 0.220, 0.225, 0.230]
y = [5.5154, 5.4669, 5.3263, 5.193, 5.0664, 4.94461, 4.8317, 4.7226, 4.6185, 4.5191, 4.4242]

h = x[1] - x[0]
x1 = 0.1
x2 = 0.9
q = (x1 - x[0])/h
q1 = (x2-x[-1])/h

value1 = 0.7868
value2 = 0.53808

def n(y, j): #обчислення кінцевих різниць

    mas=[]

    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
      return mas
    else:
       j -= 1
    return n(mas, j)

#Перша інтерполяційна формула Ньютона

s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)

#Друга інтерполяційна формула Ньютона

s1 = y[5]-q*n(y,1)[4]+q*(q-1)*n(y,2)[3]/factorial(2)
s2 = q*(q-1)*(q-2)*n(y,3)[2]/factorial(3)
s3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[1]/factorial(4)
s4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)

n_1 = s_1 + s_2 + s_3 + s_4
n_2 = s1 + s2 + s3 + s4

print('First interpolation Formula:', round(value1, 4))
print('Second interpolation Formula:', round(value2, 4))


plt.plot(x, y, '-ro')
plt.grid()
plt.show()




