# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:07:17 2016

@author: hello
"""

def longest_helper (t):
    if len(t) <= 1:
        l = 0
        h = -1
        return l, h
    else:
        left, root, right = t
        ll, hl = longest_helper(left)
        lr, hr = longest_helper(right)
        h = max (hl, hr) + 1
        l = max (ll, lr, (hl + hr + 2))
        return l, h

def longest (t):
    return longest_helper (t)[0]