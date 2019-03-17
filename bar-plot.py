#!/usr/bin/python3

import matplotlib.pyplot as plt

x=[1,2,9]
y=[3,5,7]
y1=[3,6,8]
x1=[4,8,13]


plt.title("simple")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.bar(x,y,label="water",color='g')
plt.bar(x1,y1,label="soil",color='r')    

plt.legend()
plt.grid(color='y')
plt.show()

