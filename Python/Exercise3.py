# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:44:36 2017

@author: User
"""

'''Very often, one wants to "Cast" variables of a certain type into another type.
Suppose we have variable x = '123', but really we would like x to be an integer. 
This is easy to do in python, just use desiredtype(x) e.g. int(x) to obtain an integer.
Try the following and explain the output:'''


print(float(123))  #Converts the int 123, into the equivalent value float: 123.0
print(float('123')) #Converts the string '123' into the equivalent numeric value float: 123.0
print(float('123.23')) #Converts the string '123.23' into the equivalent numeric value float: 123.23
print(int(123.23)) #Truncates the decimal to get 123
#int('123.23') 
                #Will return a value error. There is no direct integer that is equivalent to '123.23',
                #the string '123.23' must first be converted to a float, and then to a int.
print(int(float('123.23'))) #First converts the string '123.23' to the float 123.23, then truncates the decimal to get 123
print(str(12)) #Turns the integer 12, into the string '12'
print(str(12.2)) #Turns the float 12.2 into the string '12.2'
print(bool('a')) #All values except for 0 and empty data structures are equivalent to a boolean True.
print(bool(0)) # 0 is equivalent to a boolean False.
print(bool(0.1)) #All values except for 0 and empty data structures are equivalent to a boolean True.