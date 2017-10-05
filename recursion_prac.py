#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:38:01 2017

@author: j-raff
"""

#permutation of a list of int

def perm_list(list_int):
    if list_int == []:
        return [[]]
    else:
        x = perm_list(list_int[1:])
        return x + [ [list_int[0]] + y for y in x]
    
# %%

# sum of 1...n
        
def sum_n(num):
    if num == 1 or num == 0:
        return num
    else:
        return num + sum_n(num - 1)

# %%

# find and returns the minimum element in a list
        
def get_min(list_int):
    if len(list_int) == 1:
        return list_int[0]
    if list_int[0] < list_int[1]:
        return get_min(list_int[:1] + list_int[2:])
    else:
        return get_min(list_int[1:])
        
    
# %%
# find sum of list
        
def get_sum(list_int):
    if len(list_int) == 1:
        return list_int[0]
    else:
        return list_int[0] + get_sum(list_int[1:])
    
# %%

# check if string is palindrome 
        
def isPalindrome(string):
    string = string.lower().replace(' ', '')
    
    if len(string) == 1 or len(string) == 0:
        return True
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])

    else:
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    