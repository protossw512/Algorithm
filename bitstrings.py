# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:53:18 2016

@author: hello
"""
import time
import sys


def num_no(n):
    cache = None

    def find(n, cache=None):
        if cache is None:
            cache = {}
            cache[0] = 1
            cache[1] = 2
        if n in cache:
            return cache[n]
        cache[n] = find(n - 1) + find(n - 2)
        return cache[n]
    return find(n, cache)


def num_yes(n):
    k = 2**n - num_no(n)
    return k


if __name__ == "__main__":

    print num_no(10)
    print num_yes(10)
    print num_no(3)
    print num_yes(3)

    n = 1
    sys.setrecursionlimit(15000)
    for _ in xrange(18):
        starttime = time.time()
        result = num_no(n)
        print n, time.time() - starttime
        n += 2
