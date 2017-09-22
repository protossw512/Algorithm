# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:52:28 2016

@author: hello
"""
import sys
import time
import random

def best(w, a):
    bag = {}
    n = len(a)
    def find(i, bag = {0:0}):
        maxi = []
        if i in bag:
            return bag
        else:
            for j in range(n):
                if i >= a[j][0]:
                    maxi.append(find(i - a[j][0])[i - a[j][0]] + a[j][1])
                j += 1
                maxi.append(0)
            bag[i] = max(maxi)
        return bag
    bag = find(w)
    back = [0]*n
    x = w
    while x >= 1:
        for i in range(n):
            if x >= a[i][0] and bag[x] - a[i][1] == bag[x - a[i][0]]:
                back[i] += 1
                x = x - a[i][0]
                break
            i += 1 
    return bag[w],back

def best2(w, a):
    bag = {0:0}
    n = len(a)
    for x in range(0, w + 1):
        maxi = []
        for i in range(0, n):
            if x >= a[i][0]:
                maxi.append(bag[x - a[i][0]] + a[i][1])
            i += 1
            maxi.append(0)
        bag[x] = max(maxi)
    back = [0]*n
    x = w
    while x >= 1:
        for i in range(n):
            if x >= a[i][0] and bag[x] - a[i][1] == bag[x - a[i][0]]:
                back[i] += 1
                x = x - a[i][0]
                break
            i += 1
    return bag[w],back
    
    
if __name__ == "__main__":
    print best(3, [(1, 5), (1, 5)])
    print best(3, [(2, 4), (3, 5)])
    print best(3, [(1, 2), (2, 5)])
    print best(3, [(1, 2), (1, 5)])
    print best(58, [(5, 9), (9, 18), (6, 12)])
    print best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
#    
    print best2(3, [(1, 5), (1, 5)])
    print best2(3, [(2, 4), (3, 5)])
    print best2(3, [(1, 2), (2, 5)])
    print best2(3, [(1, 2), (1, 5)])
    print best2(58, [(5, 9), (9, 18), (6, 12)])
    print best2(92, [(8, 9), (9, 10), (10, 12), (5, 6)])
#    
        
#    random.seed(128)   
#    sys.setrecursionlimit(15000)
#    n = 10
#    for _ in xrange(20):
#        lst = []
#        for _ in range(n):
#            lst.append((random.randint(1, 10), random.randint(1, 10))) 
#        starttime = time.time()
#        result = best(n, lst)
#        print n, time.time()-starttime
#        n *= 2