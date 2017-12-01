# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:33:45 2017

@author: User
"""

'''
(a) Write a function that prints the elements of a list
(b) Write a function that prints the elements of a list in reverse
(c) Write your own implementation of the len function
'''

lst = [0,1,2,3,4,5,6,7,8,9]
empty = []

#a
def iterator(List):
    for element in List:
        print(element)


iterator(lst)
iterator(empty)

#b

def reverse_iterator(List):
    r = -1
    for x in range(len(List)):
        print(List[r])
        r = r-1

reverse_iterator(lst)
reverse_iterator(empty)

#c

def Length(List):
    size = 0
    for element in List:
        size = size + 1
    return size

Length(lst)
Length(empty)
        