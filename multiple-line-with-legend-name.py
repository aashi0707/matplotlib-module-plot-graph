#!/usr/bin/python3

import matplotlib.pyplot as plt

x=[1,2,3]
y=[5,6,2]
x1=[5,7,2]
y1=[10,14,19]

plt.plot(x,y,label="First line")
plt.plot(x1,y1,label="Second line")

plt.title("yayyy...i am learning it")
plt.legend()
plt.show()
