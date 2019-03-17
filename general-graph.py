#!/usr/bin/python3

import matplotlib.pyplot as plt

x=[1,2,9]
y=[3,5,7]

plt.title("simple")
plt.xlabel("x-axis")
plt.ylabel("y-label")
plt.plot(x,y,linewidth=6,label="Hello")
plt.legend()
plt.show()

