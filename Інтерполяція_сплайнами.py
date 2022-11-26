import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x = [1.3, 1.9, 2.6, 2.8, 3.1]
y = [1.63, 2.18, 1.46, 1.17, 2.95]

spl = UnivariateSpline(x, y)
xs = np.linspace(0, 4.0, 1000)
plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.show()
