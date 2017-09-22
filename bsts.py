# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:17:55 2016

@author: hello
"""

def bsts(n):
    cache = None
    def find(n, cache = None):
        if cache == None:
            cache = {}
            cache[0] = 1
            cache[1] = 1
        i = 1
        if n in cache:
            return cache[n]
        cache[n] = 0
        while i <= n:
            cache[n] = cache[n] + (find(i-1, cache) * find(n-i, cache))
            i += 1
        return cache[n]
    return find(n, cache)

if __name__ == "__main__":
    print bsts(2)
    print bsts(3) 
    print bsts(4)
    print bsts(5)
    print bsts(6)