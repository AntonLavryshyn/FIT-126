import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2, 0.1)
y = 1/2 + np.sin(x + 0.5) / 2
y1 = np.arccos(1.5 - x)

plt.plot(x, y1)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Відокремлення графічним способом')
plt.grid()
plt.show()

