# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:39:18 2016

@author: Xinyao
"""

import random

#def qselect(i,a):
#    if len(a) == 1:
#        return(a[0])
#    r= random.randint(0, len(a) - 1)
#    exchange = a[0]
#    a[0] = a[r]
#    a[r] = exchange
#    pivot = a[0]
#    left = [x for x in a if x < pivot]
#    right = [x for x in a[1:] if x >= pivot]
#    if len(left) + 1 == i:
#        return pivot
#    elif len(left) + 1 < i:
#        return qselect(i - len(left) - 1, right)
#    elif len(left) + 1 > i:
#        return qselect(i, left)
def qselect(i,a):
    if len(a) == 1:
        return(a[0])
    r= random.randint(0, len(a) - 1)
    exchange = a[0]
    a[0] = a[r]
    a[r] = exchange
    pivot = a[0][0]
    left = [x for x in a if x[0] < pivot]
    right = [x for x in a[1:] if x[0] >= pivot]
    if len(left) + 1 == i:
        return pivot
    elif len(left) + 1 < i:
        return qselect(i - len(left) - 1, right)
    elif len(left) + 1 > i:
        return qselect(i, left)
            
if __name__ == '__main__':
#    print qselect(1, [(0, 0), (-1, 5, 0, 0)])
    print qselect(10, [(-9, 0), (-9, 4, 0, 0), (-9, 7, 0, 0), (-9, 9, 0, 0), (-9, 11, 0, 0), (-9, 12, 0, 0), (-9, 16, 0, 0), (-9, 17, 0, 0), (-9, 18, 0, 0), (-8, 19, 0, 0), (-7, 20, 0, 0)])
    
    
