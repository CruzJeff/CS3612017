# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:50:15 2017

@author: User
"""

#Exercise 10
'''Plot the function f(x) = sin^2(x-2)e^(-x^2)
over the interval [0,2] with axis labels,title,etc '''

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (np.sin(x-2) ** 2) * (np.e ** (-x ** 2))



x = np.arange(0.0, 2.0, 0.01)  
y = f(x)

plt.plot(x, y)  

plt.xlabel('X')  
plt.ylabel('F(X)')  
plt.title('Exercise 10')   
plt.grid(True)   
plt.show()  

