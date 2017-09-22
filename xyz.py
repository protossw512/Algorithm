# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 16:09:35 2016

@author: hello
"""
import time, random

def main():
    print find([1, 4, 2, 3, 5])
    print find([7, 4, 5, 1, 9, 2, 25, 18])
    print find([1, 100, 2000])
    print find([3,2,1,6,7,4,9,12,10])

    n = 1
    for _ in xrange(13):
        lst = range(n)
        random.shuffle(lst)
        starttime = time.time()
        result = find(lst)
        print n, time.time()-starttime
        n *= 2


def find(a):
    a = sorted(a)
    c = []
    j = 0
    k = len(a) - 1
    for i in range (0, len(a)):
        j = 0
        k = len(a) - 1
        while k - j > 0 and k < len(a):
            if a[j] + a[k] == a[i]:
                c.append((a[j], a[k], a[i]))
                j = j + 1
                k = k + 1
            elif a[j] + a[k] < a[i]:
                j = j + 1
            else:
                k = k - 1
        i = i + 1
    return c
          
if __name__ == "__main__":      
    main()