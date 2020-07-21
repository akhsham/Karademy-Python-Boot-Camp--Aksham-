# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

user_list = input("please write your list according to this format \n"
                  "[a,b,c,d,e,f]\n"
                      "::  \n")
user_sample = input("sample: ")
for letter in user_sample:
    if letter in user_list:
        print(letter)
print(user_list)