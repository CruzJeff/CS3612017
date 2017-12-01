# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:46:25 2017

@author: User
"""

'''Consider having a list with lists as elements, eg [[1,3],[3,6]].
Write a function that takes such a list, and returns a list with
as elements the elements of the sublists, e.g [1,3,3,6]'''


List = [ [1,3],[3,6] ]
def flatten(l):
    flattened_List = []
    for vector in l:
        for element in vector:
            flattened_List.append(element)
    return flattened_List
    

New_List = flatten(List)
print(New_List)
