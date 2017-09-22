# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:45:06 2016

@author: hello
"""
import time
import sys

def fib2(n, cache=None):
    if cache is None:
        cache = {}
        cache[1] = 1
        cache[2] = 1
    if n in cache:
        return cache[n]
    i = 3
    while i <= n:
        cache[i] = cache[i-1] + cache[i-2]
        i = i + 1
    return cache[n]

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    a = fib(n-1) + fib(n-2)
    return a
        
        
        
        
if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    n = 1
    for _ in xrange(40):
        starttime = time.time()
        result = fib(n)
        print n, time.time()-starttime
        n += 1