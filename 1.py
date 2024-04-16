import numpy as np
import matplotlib.pyplot as plt


def Y(x):
    return 5 * np.sin(10*x) * np.sin(3*x)


x_values = np.linspace(0, 4, 1000)

y_values = Y(x_values)


plt.plot(x_values, y_values)
plt.title('Графік функції Y(x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.grid(True)


plt.savefig('function_plot.png')


plt.show()
