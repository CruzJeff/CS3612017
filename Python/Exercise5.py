# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:27:03 2017

@author: User
"""

'''Use a while loop to find the first 20 numbers that are 
divisible by 5,7, and 11 and print them '''


counter = 0
x = 5 * 7 * 11 #This will be the first number that is divisible by all 3
while (counter < 20):
    if (x % 5 == 0 and x % 7 == 0 and x % 11 == 0):
        print(x)
        counter = counter + 1
    x += 11 #We can increment by 11 to be as efficient as possible. 