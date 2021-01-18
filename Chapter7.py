# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:16:56 2020

@author: giris
"""

#print(list(range(0, 2000)))
def hellofunc(myname):
    print("Hello ", myname)
    
hellofunc("Wondushi")

def variable_test():
    first = 10
    second = 20
    return first * second 

print(variable_test())



import sys
print(sys.stdin.readline())