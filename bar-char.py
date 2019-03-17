#!/usr/bin/python3

import matplotlib.pyplot as plt

x=[1,2,3]
y=[5,6,2]
y1=[10,1,19,2]
x1=[5,7,2,9]

plt.bar(x1,y1,label="Bar chart is launching")
plt.bar(x1,y1,label="Bar chart is launching",color='r')       # if you want to change color of bar


plt.xlabel("x1")
plt.ylabel("y1")

plt.title("yayy..i have learnt it")
plt.legend()
plt.show()

