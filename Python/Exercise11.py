# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:52:43 2017

@author: User
"""


'''Write two functions, one that uses iteration, and the other using recursion
that achieve the following:
    The input of the function is a list with numbers. 
    The function returns the product of the numbers in the list. '''
    
    
def iterative_mul(List):
    if len(List) == 0:
        return 0
    result = 1
    for element in List:
        result = result * element
    return result


def recursive_mul(List):
    if len(List) == 0:
        return 0
    if len(List) == 1:
        return List[0]
    else:
        return recursive_mul([List[0]]) * recursive_mul(List[1:])


List = [1,2,3,4,5,6,7,8,9,10]
empty = []
iterative_mul(List)
recursive_mul(List)
iterative_mul(empty)
recursive_mul(empty)