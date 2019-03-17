#!/usr/bin/python3.6

import matplotlib.pyplot as plt
import tkinter 
a=range
x=[2,8,4]
x1=[12,18,15]
y=[9,6,7]
y1=[19,16,17]

plt.xlabel("time")
plt.ylabel("distance")
plt.scatter(x,y)
plt.scatter(x1,y1)
plt.grid()
plt.show()
