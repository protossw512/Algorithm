# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:29:47 2016

@author: hello
"""

def tsp(a):
    n = len(a)
    s = ()
    opt = defaultdict(lambda: 999999)
    opt[(1), 1] = 0
    def _tsp(j, s, opt):
        if (s, j) in opt:
            return opt[s, j]
# No idea how to do the rest steps
    
    
if __name__ == "__main__":
    a = {(0,0): 0, (0,1): 3, (1,0): 3, (1,1): 0}
    b = {(0,0): 0, (0,1): 4, (0,2): 3, (1,0): 4, (1,1): 0, (1,2): 7, (2,0): 3, (2,1): 7, (2,2): 0}
    c = {(0,0): 0, (0,1): 10, (0,2): 6, (1,0): 10, (1,1): 0, (1,2): 2, (2,0): 6, (2,1): 2, (2,2): 0}