# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:23:54 2020

@author: giris
"""

## Problem 1 
def print_rectangle(length, width):
   area = length * width
   perimeter = length + length + width + width
   print("Area = ", area, ", Perimeter = ", perimeter)
   

def print_rect():
    length = int(input("Please enter length: "))
    width = int(input("Please enter width: "))
    area = length * width
    perimeter = length + length + width + width 
    print("Area = ", area, ", Perimeter = ", perimeter)


## Problem 2
import math
def print_circle(radius):
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    print(f"Area = {area:.2f} Perimeter = {perimeter:.2f}")


def print_cir():
    radius = int(input("Please enter radius: "))
    area = math.pi * radius**2
    print(f"Area = {area:.2f} Perimeter = {perimeter:.2f}")


## Problem 3 
def print_sum(n):
    sum = 0
    for x in range(1, n+1):
        sum = sum + x
    print("The sum from numbers 1 to ", n, "= ", sum) 


def print_summation():
    n = int(input("Please enter n: "))
    sum = 0
    for x in range(1, n+1):
        sum = sum + x
    print("The sum from numbers 1 to ", n, "= ", sum) 


## Problem 4
def print_factorial(n):
    factorial = 1
    for x in range(1, n+1):
        factorial = factorial * x
    print(n, "! = ", factorial)


def print_fact():
    n = int(input("Please enter n: "))
    factorial = 1
    for x in range(1, n+1):
        factorial = factorial * x
    print(n, "! = ", factorial)


##Problem 5
def print_sum_froma_tob(least_number, greatest_number):
    n = greatest_number - least_number + 1
    sum_froma_tob = ((least_number + greatest_number) * n)/2
    print("The sum from", least_number, "to", greatest_number, "=", sum_froma_tob)

def sum_froma_tob():
    least_number = int(input("Please enter the least number a: "))
    greatest_number = int(input("Please enter the greatest number b: "))
    while(least_number > greatest_number):
        print("Error: Please enter a < b")
        least_number = int(input("Please enter the least number a: "))
        greatest_number = int(input("Please enter the greatest number b: "))
    n = greatest_number - least_number + 1
    sum_froma_tob = ((least_number + greatest_number) * n)/2
    print("The sum from", least_number, "to", greatest_number, "=", sum_froma_tob)


##Problem 6 
def print_product_froma_tob(least_number, greatest_number):
    product = 1
    for x in range(least_number, greatest_number+1):
        product = product * x
    print("The product from", least_number, "to", greatest_number, "=", product)

def product_froma_tob():
    least_number = int(input("Please enter the least number a: "))
    greatest_number = int(input("Please enter the greatest number b: "))
    while(least_number > greatest_number):
        print("Error: Please enter a < b")
        least_number = int(input("Please enter the least number a: "))
        greatest_number = int(input("Please enter the greatest number b: "))
    product = 1
    for x in range(least_number, greatest_number+1):
        product = product * x
    print("The product from", least_number, "to", greatest_number, "=", product)

def product_from_b_to_a():
    least_number = int(input("Please enter the least number a: "))
    greatest_number = int(input("Please enter the greatest number b: "))
    if(least_number > greatest_number):                
        product = 1
        for x in range(greatest_number, least_number+1):
            product = product * x
        print("The product from", greatest_number, "to", least_number, "=", product)
    else:
        product = 1
        for x in range(least_number, greatest_number+1):
            product = product * x
        print("The product from", least_number, "to", greatest_number, "=", product)

##Problem 7
def print_fibonacci(n):
    if (n <= 0):
        print("Error: Please enter n greater than 0.")
        return
    if (n == 1):
        print("Fibonacci series up to 1 = 1")
        return
    if (n == 2):
        print("Fibonacci series up to 2 = 1, 1")
        return
    for x in range(3, n+1):
        Fx = Fxm1 + Fxm2
        Fxm1 = Fx
        Fxm2 = Fxm1
    print("Fibonacci series up to", n, "=", )





## Function calls ##

# print_rectangle(5, 10)       
# print_rect()
# print_circle(7)  
# print_cir()
# print_sum(5)
# print_summation()
# print_factorial(5)
# print_fact()
# print_sum_froma_tob(5, 7)
# sum_froma_tob()
# print_product_froma_tob(2, 4)
# product_froma_tob()
# product_from_b_to_a()
print_fibonacci(3)