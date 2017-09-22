# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 23:07:30 2016

@author: hello
"""
import heapq

def kmergesort(a, k):
    c = []
    n = len(a)
    length = len(a)/k if len(a) >=k else 1
    for i in range(0, k-1):
        j = (i*length+length)
        e = i*length
        if a[e:j] != []:
            c.append(a[e:j])
        i += 1
    if n > k:
        l = (k-1)*length
        c.append(a[l:])
    if len(c[1]) <= 1:
        return c
    else:
        for i in range(0, len(c)):
            if len(c[i]) <= 1:
                return c[i]
            c[i] = merge(kmergesort(c[i], k), len(c[i]))
    return merge(c, n)
    
def merge(a, n):
#    if len(a[0]) <=1:
#        return a
    b = []
    temp = []
    for lst in a:
        heapq.heappush(temp, [lst[0], a.index(lst)])
        lst.pop(0)
    while len(b) < n:
        c = heapq.heappop(temp)
        b.append(c[0])
        if a[c[1]] != []:
            heapq.heappush(temp, [a[c[1]][0], c[1]])
            a[c[1]].pop(0)
    return b

if __name__ == "__main__":
    print kmergesort([1,4,2,3,6,5,7,8,10], 4)
    print kmergesort([4,1,5,2,6,3,7,0], 3)