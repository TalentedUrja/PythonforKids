# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:54:54 2020

@author: urja
"""

print("Hello world!!!")
N = input("How many times do you want to print?\n")
N = int(N)
for index in range(1,N+1):
    print("Happy Birthday Saina!")
    

N = input("I can find the sum of numbers up to N. Please type N and press enter.")
N = int(N)
Sum = 0
for index in range(1,N+1):
    Sum = Sum + index
    
print("The sum is equal to ", Sum)
    
    