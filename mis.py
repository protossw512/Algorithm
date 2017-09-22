# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:48:21 2016

@author: hello
"""
import time
import sys
#    

def max_wis(a):
    cache = None
    solution = []
    def find(n, cache = None):
        if cache == None:
            cache = {}
            cache[-2] = 0
            cache[-1] = 0
        if n in cache:
            return cache
        if a[n] + find(n-2,cache)[n-2] >= find(n-1,cache)[n-1]:
            cache[n] = a[n] + find(n-2,cache)[n-2] 
        else:
            cache[n] = find(n-1,cache)[n-1]
        return cache
    n = len(a) - 1
    cache = find(n,cache)
    i= len(a) - 1
    while i >= 0:
        if cache[i - 2] + a[i] <= cache[i - 1]:
            i = i - 1
        else:
            solution.append(a[i])
            i = i - 2
    solution.reverse()
    return cache[n], solution
        

def max_wis2(a):
    solution = []
    cache={}
    cache[-2]=0
    cache[-1]=0
    if a == []:
        return (0, [])
    for n in range(0, len(a)):
        if a[n] + cache[n-2] >= cache[n-1]:
            cache[n] = a[n] + cache[n-2]
        else:
            cache[n] = cache[n-1]
        n += 1
    i = len(a) - 1
    while i >= 0:
        if cache[i - 2] + a[i] <= cache[i - 1]:
            i = i - 1
        else:
            solution.append(a[i])
            i = i - 2
    solution.reverse()            
    return cache[n - 1], solution   

    

if __name__ == "__main__":
    print max_wis([7,8,5])
    print max_wis([-1,8,10])
    print max_wis([])
    print max_wis([-1,-2,-3,-5])
    print max_wis([-1,-5,-2,-7,0,3,1,2,6,4,3,2,6,9])
    print max_wis(range(100,-1,-1))
#    print max_wis2([7,8,5])
#    print max_wis2([-1,8,10])
#    print max_wis2([])
#    print max_wis2([-1,-2,-3,-5])
#    print max_wis2([-1,-5,-2,-7,0,3,1,2,6,4,3,2,6,9])
#    print max_wis2(range(100,-1,-1))
#    n = 1
#    sys.setrecursionlimit(15000)
#    for _ in xrange(20):
#        lst = range(n)
#        starttime = time.time()
#        result = max_wis2(lst)
#        print n, time.time()-starttime
#
#        n *= 2