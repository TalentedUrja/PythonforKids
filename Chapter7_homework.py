# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:40:22 2020

@author: giris
"""

#1: Basic Moon Weight Function
#def moon_weight(start_weight, gain_per_year):
#    for year in range (1, 16):
#        weight = start_weight + gain_per_year * year
#        print("Year =", year, "and", "Weight =", weight)
#
#moon_weight(30, 0.25)


'''
Expected output if start_weight=15, gain_per_year=2 
    year 1, weight = 17
    year 2, weight = 19
    year 3, weight = 21
    :
    year 15, weight = 45
    
    number_of_years=5, in the for loop you want (1,6)
    number_of_years=20, in the for loop you want (1,21)
    number_of_years=15, in the for loop you want (1,16)
'''

def moon_weight():
    start_weight = float(input("Please enter start weight:"))
    gain_per_year = float(input("Please enter gain per year:"))
    number_of_years = int(input("Please enter number of years:"))
    
    for year in range (1, number_of_years+1):
        weight = start_weight + gain_per_year * year
        print("year ", year, ", weight = ", weight)

def alt_moon_weight(start_weight, gain_per_year):
    current_weight = start_weight
    for year in range (1, 16):
        current_weight = current_weight + gain_per_year
        print("year ", year, ", weight = ", current_weight)

moon_weight()
#moon_weight(30, 0.25, 20)
#alt_moon_weight(30, 0.25)



        