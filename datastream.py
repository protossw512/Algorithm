G# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:43:38 2016

@author: hello
"""
import time
import heapq

def ksmallest(k, a):
    c = []
    d = []
    for i in range(0, len(a)):
        if len(c) < k:
            heapq.heappush(c, -a[i])
        elif -a[i] > c[0]:
            heapq.heapreplace(c, -a[i])
        i += 1
    while c != []:
        d = d + [-heapq.heappop(c)]
    return d[::-1]

if __name__ == "__main__":
    print ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
    print ksmallest(3, xrange(1000000, 0, -1))
    print ksmallest(5, [-3,-5,-1,-8,-11,20,1,3,2,4,4,4,4,4])
    print ksmallest(5, xrange(1000000, -100001, -1))
    print ksmallest(5, [0,0,0,-1,1,1,1,2,3,3,3,2,4])
    
    n = 1
    for _ in xrange(7):
        lst = range(n)
        lst = lst[::-1]
#        random.shuffle(lst)
        starttime = time.time()
        a = []
        ksmallest(50, lst)
        print n, time.time()-starttime
        n *= 10