# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:12:55 2016

@author: hello
"""

from collections import defaultdict

def order(n, a):
    inedges = defaultdict(list)
    outedges = defaultdict(list)
    for (u, v) in a:
        inedges[v].append(u)
        outedges[u].append(v)
    initial = range(n)
    result = []
    while initial != []:
        for node in initial:
            loop = True
            if inedges[node] == []:
                loop = False
                result.append(node)
                initial.remove(node)
                lst = outedges[node]
                for nodes in lst:
                    inedges[nodes].remove(node)
                break 
        if loop == True:
            return None
    return result, outedges

#def longest(n, a):
#    sort = order(n, a)
#    left = {}
#    right = {}
#    opt = defaultdict(int)
#    back = {}
#    for x in xrange(n):
#        back[x] = -1
#    for edges in a:
#        left[edges], right[edges] = edges
#    for v in sort:
#        for edge in a:
#            if left[edge] == v:
#                u = right[edge]
#                if opt[v] + 1 > opt[u]:
#                    opt[u] = opt[v] + 1
#                    back[u] = v
#    max_key = max(opt, key=lambda k: opt[k])
#    return max(opt.values()), solution(max_key, back, a)

def longest(n, a):
    sort, adjlist = order(n, a)
    opt = defaultdict(int)
    back = {}
    for x in xrange(n):
        back[x] = -1
    for v in sort:
        for u in adjlist[v]:
            if opt[v] + 1 > opt[u]:
                opt[u] = opt[v] + 1
                back[u] = v
    max_key = max(opt, key=lambda k: opt[k])
    return max(opt.values()), solution(max_key, back, a)


def solution(v, back,a):
    result = []
    if v not in back:
        result = []
        return result
    result = solution(back[v], back, a) + [v]
    return result

if __name__ == "__main__":
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
     
