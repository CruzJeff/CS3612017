# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:20:22 2017

@author: User
"""


#Exercise 13
'''Write a Python program that extracts the email addresses of a file. 
An email file emails.txt is provided to test your program.'''

import re

file = open('emails.txt','r')
file = file.read()

Email_Addresses = re.findall(r'([^ ]+[@][^ ]+[.][a-z]+)', file)
print(Email_Addresses)

