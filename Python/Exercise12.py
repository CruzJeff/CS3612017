# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 17:03:55 2017

@author: User
"""

'''There was no question asked this for exercise. But I assume 
it wants you to write the fibonacci function'''

fiblist = [0 for x in range(999)] #Using a list for memoization

def fib(x):
    if x == 0:
        fiblist[x] = 0
        return 0
    elif x == 1:
        fiblist[x] = 1
        return 1
    elif x == 2:
        fiblist[x] = 2
        return 2   
    elif fiblist[x] != 0.0:
        return fiblist[x]
    else:
        fiblist[x] = fib(x-1) + fib(x-2)
        return fiblist[x]
    

for x in range(50):
    print(fib(x))



#Due to Python 3's arbitrary precision, this function will never overflow
#The only limit will be the size of the fiblist used for memoization