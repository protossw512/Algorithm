# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 13:33:13 2016

@author: hello
"""
from collections import defaultdict

def best(W, items):
    n = len(items)
    back = defaultdict(int)
    opt=defaultdict(lambda : 9999999)
    for m in range (n):
        opt[0, m] = 0
    def _best(x, i):

        if i <= 0 or (x, i) in opt:
            return opt[x, i]
        v = items[i - 1]
        j = 0
        while x - j * v >= 0:
            ans = _best(x - j * v, i - 1) + min(1, j)
            if opt[x, i - 1] >= ans:
                opt[x, i] = ans
                back[x, i] = j
            j += 1
        return opt[x, i]
    return (_best(W, n), solution(W, n - 1, back, items)) if _best(W, n) != 9999999 else "None"

    
def solution(x, i, back, items):
    if i < 0:
        return []
    j = back[x, i + 1]
    v = items[i]
    return solution(x - v*j, i-1, back, items) + [j]


if __name__ == "__main__":
    print best(47, [6, 10, 15])
    print best(59, [6, 10, 15])
    print best(37, [4, 6, 15])
    print best(27, [4, 6, 15])
    print best(75, [4, 6, 15])
    print best(17, [2, 4, 6])
    print best(8, [4, 3])

    