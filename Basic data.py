# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:54:27 2020

@author: giris
"""

subject_list = ["Math", "Science", "LA/SS" , "PE"]
teacher_list = ["Harder",  "Drake", "Kirkman/Damey", "Lidstrum"]
subject_list.append("Music")
print(subject_list)
subject_list.remove("PE")
print(subject_list) 
subject_list.sort()
print(subject_list)
print(len(subject_list))
print(teacher_list)
print(teacher_list[0])

teacher_map = {"Math":"Harder", "Science":"Drake"}
print(teacher_map["Math"])



