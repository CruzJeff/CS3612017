# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 22:24:27 2017

@author: User
"""

#Explain the output of the following code:
    
#A----------------------------------------------------------------------------------------------#
print(5/3) 
'''Returns 1.6666666666666667 in Python 3. In Python 2 it would return 1
In Python 3, division always returns a float. However, in Python 2, dividing two ints would return an int.
to mimic this behavior in Python 3, you would use // which is floored division.'''
          
#B---------------------------------------------------------------------------------------------#
      
print(5%3) #Returns 2. This is 5 mod 3, which is 2. The remainder when 5 is divided by 3 is 2

#C---------------------------------------------------------------------------------------------#

print(5.0/3) 
'''Returns 1.6666666666666667 in both Python 2 and Python 3. 
Since this is a float divided by an int, it returns a float in python 2.
In Python 3, division always returns a float, so this is the same as 5/3'''
#D---------------------------------------------------------------------------------------------#
            

print(5/3.0) 
'''Returns 1.6666666666666667 in both Python 2 and Python 3. 
Since this is a float divided by an int, it returns a float in python 2.
In Python 3, division always returns a float, so this is the same as 5/3'''

#E--------------------------------------------------------------------------------------------#
            
print(5.2%3) 
'''Returns 2.2. This is 5.2 mod 3, which is saying what is the remainder when 5.2 
is divided by 3, which is 2.2 '''

#-------------------------------------------------------------------------------------------------#