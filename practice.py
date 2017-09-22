# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:11:59 2016

@author: hello
"""



'''def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot]
		right = [x for x in a[1: ] if x >= pivot]
		return sort(left) + [pivot] + sort(right)
  '''

''' def sort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1: ] if x >= pivot]
    return sort(left) + [pivot] + sort(right)
'''

import random

def qselect(i, a):
    if len(a) == 1:
        return a[0]
    r= random.randint(0, len(a) - 1)
    exchange = a[0]
    a[0] = a[r]
    a[r] = exchange
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    if len(left) + 1 == i:
        return pivot
    elif len(left) + 1 < i:
        return qselect(i - len(left) - 1, right)   
    elif len(left) + 1 > i:
        return qselect(i, left)


def sort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1: ] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]

def sorted(a):
    if a == []:
        return a
    left, node, right = a
    return sorted(left) + [node] + sorted(right)

def _search(a, i):
    if a == []:
        return a
    else:
        left, node, right= a
        if i == node:
            return a
        elif i <= node:
            return _search(left, i)
        elif i > node:
            return _search(right, i)

def search(a, i):
    if _search(a, i) == []:
        return False
    else:
        return True

def insert(a, i):
    r = _search(a, i)
    if r == []:
        r += [[], i, []]

def insertionSort(a, i=1):
    if i >= len(a):
        return a
    if a[i - 1] > a[i]:
        temp = a[i]
        for j in range(0, i):
            if a[j] > temp :
                a.insert(j, temp)
                del a[i + 1]
                break
    return insertionSort(a, i + 1)

def insertion(a, i = 1):
    if i >= len(a):
        return a
    if a[i - 1] > a[i]:
        temp = a[i]
        for j in range (0, i):
            if a[j] > temp:
                a.insert(j, temp)
                del a[i + 1]
                break
    return insertion(a, i + 1)
            