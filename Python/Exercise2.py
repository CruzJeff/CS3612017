# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 22:35:23 2017

@author: User
"""


#Explain the output of the following statements:
    

#A----------------------------------------------------------------------------------------------#

#print(2000.3 ** 200) 
'''Causes an overflow. Floats in python do not have arbitrary precision (infinite length) like ints do.
importing the decimal library will allow floats with arbitrary precision'''
                    
#B---------------------------------------------------------------------------------------------#
print(1.0 + 1.0 - 1.0) # Returns 1.0, subtracting floats will return a float.


#C---------------------------------------------------------------------------------------------#
print(1.0 + 1.0e20 - 1.0e20) 
FirstStep = 1.0 + 1.0e20
print(FirstStep)
print(FirstStep - 1.0e20)
'''This returns 0. Because it first evaluates 1.0 + 1.0e20
which returns 1.0e20 because of how it is rounded. 
It then does 1.0e20 - 1.0e20 which is 0.0 '''

#-------------------------------------------------------------------------------------------------#