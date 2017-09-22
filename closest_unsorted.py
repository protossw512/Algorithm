# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 15:53:10 2016

@author: hello
"""

from __future__ import division
import time, random

def main():
    print find([4,1,3,2,7,4], 5.2, 2)
    print find([4,1,3,2,7,4], 6.5, 3)
    print find([7, 4, 5, 1, 9, 2, 25, 18], 24, 2)
    print find([1, 100, 2000], 2000, 2)
    print find([3,2,1,6,7,4,9,12,10], -2, 3)

    n = 1
    for _ in xrange(7):
        lst = range(n)
        random.shuffle(lst)
        starttime = time.time()
        result = find(lst, n/2, 5)
        print n, time.time()-starttime
        n *= 10

from random import randint
def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0],a[pindex] = a[pindex],a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            qselect(k-lleft-1, right)

def find(l, num, i):
    b = []
    c = []
    l1 = [abs(x - num) for x in l]
    l2 = l1[:]
    for j in range (1, i + 1):
        b.append(qselect(j, l2))
    bool_array = [False] * len(l)
    for j in range (0, len(b)):
        for r in range (0, len(l1)):
            if b[j] == l1[r] and bool_array[r] == False:
                bool_array[r] = True
    for j in range (0, len(l)):
        if bool_array[j] == True:
            c.append(l[j])
    return c

if __name__ == "__main__":      
    main()