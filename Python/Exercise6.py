# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 17:53:59 2017

@author: User
"""

import math

# (a) Write a function is_prime(n) that returns True if n is prime
def is_prime(x):
    if (x == 2):
        return True
    elif (x % 2 == 0):
        return False
    elif (x > 2):
        for n in range(3, math.floor(math.sqrt(x))+ 1, 2):
            if (x % n == 0):
                return False
        else:
            return True
    else:                        
        return False       


# (c) Write a function that returns all primes up to n
def sieve_of_eratosthenes(lim):
    if lim < 0:
        print("Error")
    Primes = []
    A = [0 for x in range(lim)]
    A[0] = 1
    A[1] = 1
    MAX = math.floor(math.sqrt(lim))
    for i in range(2,MAX+1):
        if A[i] == 0.0:
            for j in range(i*i,lim,i):
                A[j] = 1
    for x in range(len(A)):
        if A[x] == 0:
            Primes.append(x)
    return Primes

#Testing the function
all_primes_up_to_999 = sieve_of_eratosthenes(999)
print(all_primes_up_to_999)

#Verify with part (a) to make sure (c) is correct
for x in all_primes_up_to_999:
    if is_prime(x) == False:
        print("Error", x, "is not prime")

#(d) write a function that returns the first n primes
def first_n_primes(n):
    if n < 0:
        print("Error")
    elif n == 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2,3]
    else:
        result = [2,3]
        counter = 2
        x = 0
        while (counter < n):
            test = 6 * x + 1
            test2 = 6 * x - 1
            if is_prime(test2) == True:
                result.append(test2)
                counter = counter + 1
    
            if is_prime(test) == True:
                if counter < n:
                    result.append(test)
                    counter = counter + 1
                    
            x = x + 1
        return result

#Testing the function
first_100_primes = first_n_primes(100)
print(first_100_primes)

#Verify with (a) that (d) is correct
for x in first_100_primes:
    if is_prime(x) == False:
        print("Error", x, "is not prime")

    
#Verify with (c) that (d) is correct
for x in range(100):
    if first_100_primes[x] != all_primes_up_to_999[x]:
        print("Error")
