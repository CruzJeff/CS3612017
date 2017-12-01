# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:21:53 2017

@author: User
"""

'''Type range(5) in the interpreter, what does the interpreter return?
So what does for i in range(5) mean?

Let's also find out whether the interpreter can help us understand the object 'range(5)' better.
Type type(range(5)) in the interpreter'''


range(5) #Returns range(0,5)

#for i in range(5) means to iterate through the range(0,5) including 0,
#but not including 5.

for i in range(5):
    print(i)
    
#The above will print:
    #0
    #1
    #2
    #3
    #4
    
type(range(5)) #This is an object of type "range"