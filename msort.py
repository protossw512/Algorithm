# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:21:48 2016

@author: hello
"""

def merge(x, y):
    t = []
    while ((x != []) and (y != [])):
        if x[0] <= y[0]:
            t.append(x[0])
            x.pop(0)
        else:
            t.append(y[0])
            y.pop(0)
    if (x == [] and y != []):
        t = t + y
    elif (x != [] and y == []):
        t = t + x
    return t
            
        

def mergesort(t):
    if len(t) > 1:
        left = t[0 : len(t)/2]
        right = t[len(t)/2: ]
        left = mergesort(left)
        right = mergesort(right)
        t = merge(left, right)
    return t
