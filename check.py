from code import lagrange, xnew, x, y
import matplotlib.pyplot as plt


f = lagrange(x, y)
fig = plt.figure(figsize=(10, 8))
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange Polinomial2.0')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()