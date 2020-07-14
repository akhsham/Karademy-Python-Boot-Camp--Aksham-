#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:32:42 2020

@author: darian
"""

num1 = int(input("please insert a number: "))
num2 = int(input("please insert another number: "))

operator = int(input("Please select operator: \n"
                     "1 => Add      [A + B] \n"
                     "2 => Subtract [A - B]\n"
                     "3 => Multiply [A * B]\n"
                     "4 => Divide   [A / B]\n"
                     ":"
                     ))

def add (input1 , input2):
    return (input1 + input2)
def sub (input1 , input2):
    return (input1 - input2)
def mlt (input1 , input2):
    return (input1 * input2)
def dev (input1 , input2):
    return (input1 / input2)
if operator == 1:
    print("RESULT: " , add( num1 , num2 ))   
if operator == 2:
    print("RESULT: " , sub( num1 , num2 ))
if operator == 3:
    print("RESULT: " , mlt( num1 , num2 ))
if operator == 4:
    print("RESULT: " , dev( num1 , num2 ))
    
    
    
    


