# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:41:29 2017

@author: User
"""

# (a) Create a list with some entries
a = [0,1,2,3,4,5]

# (b) Now set b = a
b = a

# (c) Change b[1]
b[1] = 42

# (d) What happened to a?
print(a) #a[1] also got changed to 42

# (e) Now set c = a[:]
c = a[:]

# (f) Change c[2]
c[2] = 42

# (g) What happened to a?
print(a) #a remained unchanged

'''Now create a function set_first_elem_to_zero(l) 
that takes a list, sets its first entry to zero,
and returns the list '''

def set_first_elem_to_zero(l):
    l[0] = 0
    return l

test_list = [1,1,1,1]
set_first_elem_to_zero(test_list)

#What happened to the list?
print(test_list) #The first element got changed to 0

