#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:31:21 2020

@author: darian
"""

import sys
error_message = "please restart the code and write a NUMBER this time"

input_elements_raw = input("how many numbers does your list have? " )
if input_elements_raw.isdigit():
    input_elements = int(input_elements_raw)
else:
    sys.exit(error_message)

#=======================================================
    
user_list = []
for i in range(0 , input_elements):
    print("number " , i+1 , ": ")
    try:
        list_values = float(input())
    except:
        raise ValueError (error_message) 
    user_list.append(list_values)

#=======================================================

try:
    input_number = float(input("please write the number which you want test: "))
except:
    raise ValueError (error_message)
    
#=======================================================
temp = []
for list_index in range(0 , input_elements):
    temp_num = input_number - user_list[list_index]
    temp.append(temp_num)
for match_numbers in range(len(temp)):
    if temp[match_numbers] in user_list:
        print (temp[match_numbers] , user_list[match_numbers])
        


  
#=======================================================

    
     









