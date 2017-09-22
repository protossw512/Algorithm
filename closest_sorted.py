# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 22:01:56 2016

@author: hello
"""
from __future__ import division
import bisect
import time

def main():
    print find([1,2,3,4,4,7], 5.2, 2)
    print find([1,2,3,4,4,7], 6.5, 3)
    print find([1,2,3,4,4,6,6], 5, 3)
    print find([1,2,3,4,4,5,6], 4, 5)
    print find([1,2,3,4,4,5,6], 6.2, 1)
    print find([1,2,3,4,4,5,6], -1, 2)
    print find([7, 9, 11, 15, 16, 17, 33, 92], 15, 5)
    print find([1, 100, 2000, 30000, 52132], 2000, 2)
    print find([2, 5, 7, 12, 16], -2, 3)

    n = 1
    for _ in xrange(8):
        lst = range(n)
        starttime = time.time()
        result = find(lst, 30000, 5)
        print n, result, time.time()-starttime
        n *= 10

def find(l, num, i):
    ## if the list is smaller than i, then the list is too short to give enough numbers
    if i > len(l):
        print "list is too short"
        return
    ## if the number is larger than the largest number in the list, then we return i numbers from right to left
    p1 = bisect.bisect(l, num)
    if p1 >= len(l):
        return l[-i:]
    p2 = p1 + 1
    left = []
    right = []
    output = []
    for i in range (0, i):
        if  p2 >= len(l) or ((num - l[p1]) <= (l[p2] - num) and p1 >= 0):
            left.append(p1)
            p1 = p1 - 1
        elif (num - l[p1]) > (l[p2]-num):
            right.append(p2)
            p2 = p2 + 1
    left = left[::-1]
    if left != []:
        for i in range (0, len(left)):
            output.append(l[left[i]])
    if right != []:
        for i in range (0, len(right)):
            output.append(l[right[i]])
    return output


if __name__ == "__main__":      
    main()