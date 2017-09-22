# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:39:18 2016

@author: Xinyao
"""

def sort(a):
	if a == []:
		return []
	else:
		pivot = a[0]
		left = [x for x in a if x < pivot]
		right = [x for x in a[1: ] if x >= pivot]
		return [sort(left)] + [pivot] + [sort(right)]
		

def sorted(t):
    if t==[]:
        return []
    else:
      left, root, right = t
      return sorted(left) + [root] + sorted(right)

def _search(t, x):
    if t==[]:
        return t
    else:
      left, root, right = t
      if root == x:
          return [left] + [root] + [right]
      elif root < x:
          return _search(right, x)
      elif root > x:
          return _search(left, x)

def search(t, x):
    if _search(t, x) == []:
        return False
    else:
        return True

def insert(t, x): 
    r = _search(t, x)
    if r == []:
        r += [[], x, []]

            

        