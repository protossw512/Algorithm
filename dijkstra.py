# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:00:40 2016

@author: hello
"""
from collections import defaultdict
    
def shortest(n, a):
    visited = []
    unvisited = range(n)
    left = {}
    right = {}
    cost = {}
    opt = defaultdict(lambda: 9999999)
    opt[0] = 0
    back = {}
    for x in xrange(n):
        back[x] = -1
    for edges in a:
        left[edges], right[edges], cost[edges] = edges
    while unvisited != []:
        v = "inf"
        for node in unvisited:
            if opt[node] < v:
                v = node
        for edge in a:
            if left[edge] == v:
                u = right[edge]
                if opt[v] + cost[edge] < opt[u]:
                    opt[u] = opt[v] + cost[edge]
                    back[u] = v
            if right[edge] == v:
                u = left[edge]
                if opt[v] + cost[edge] < opt[u]:
                    opt[u] = opt[v] + cost[edge]
                    back[u] = v
        visited.append(v)
        unvisited.remove(v)
    return opt[n - 1], solution(n - 1, back, a)

def solution(v, back,a):
    result = []
    if v not in back:
        result = []
        return result
    result = solution(back[v], back, a) + [v]
    return result 

if __name__ == "__main__":
    print shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])