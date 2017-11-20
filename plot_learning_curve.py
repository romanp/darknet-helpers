#!/usr/bin/python
"""Plot learning curve given Darknet's textual training output."""

#imports
import numpy as np
from matplotlib import pyplot as plt

#main
avg_lst = []
file = open("train.out",'r')
for line in file:
    if "avg" in line:
        data = line.split()
        avg_lst = np.append(avg_lst, float(data[2]))
file.close()
print(avg_lst)
plt.plot(avg_lst,'b')
plt.xlabel("epochs")
plt.ylabel("AVG training loss")
plt.title("learning curve")
plt.show()
