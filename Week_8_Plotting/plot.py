# plot.py
# plot the function y = x^2
# Author: Andy Walker

import numpy as np
import matplotlib.pyplot as plt 

xpoints = np.array(range(-101,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()