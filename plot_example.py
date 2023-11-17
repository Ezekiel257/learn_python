#importing matplotlib
import matplotlib

#print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([12, 6, 5, 9])
ypoints = np.array([5, 45, 12, 6])

plt.plot(xpoints, ypoints)
#plt.show()

#using histograms
import numpy as np

x = np.random.normal(170, 10, 250)

print(x)

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 
