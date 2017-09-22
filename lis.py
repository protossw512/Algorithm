# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 12:54:18 2016

@author: hello
"""
from collections import defaultdict

def lis(a):
    opt = defaultdict(lambda: 1)
    back = {}
    a = a + "\xff"
    n = len(a)
    def _lis(j, opt):
        if j in opt:
            return opt[j]
        for k in range(j):
            if ord(a[k]) < ord(a[j]):
                ans = _lis(k, opt) + 1
                if ans > opt[j]:
                    opt[j] = ans
                    back[j] = k
        return opt[j]
    _lis(n - 1, opt)
    result = max(opt.items(), key=lambda k: k[1])
    return solution(result[0], back, a)[:-1]

def solution(j, back,a):
    result = ""
    if j not in back:
        result = a[j]
        return result
    result = solution(back[j], back, a) + a[j]
    return result

if __name__ =="__main__":
    print lis("aebbcg")
    print lis("aebbcgab")
    print lis("zdaebbcgab")
    print lis("zyx")
    print lis("eaebbcg")
    print lis("abcdefg")
    print lis("aabbccddeeccffggaabbccddeeffgghheeiiabc")
    print lis("saggfedcba")