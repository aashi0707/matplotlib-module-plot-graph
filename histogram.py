#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(size=1000)
plt.hist(x,normed=True,bins=30)
plt.ylabel('probability')
plt.show()

