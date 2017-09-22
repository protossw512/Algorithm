# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:11:03 2016

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
    return result





def order2(n, a):
    left  = {}
    right = {}
    sort = []
    for edges in a:
        left[edges], right[edges] = edges
    nodes = range(n)
    while len(sort) < n:
        for i in nodes:
            loop = True
            if i not in right.values():
                loop = False
                sort.append(i)
                nodes.remove(i)
                for edge in a:
                    if left[edge] == i:
                        del right[edge]
                break
        if loop == True:
            return None
    return sort

#def order(n, a):
#    graph = {}
#    sort = []
#    for i in range (n):
#        graph[i] = []
#    for edges in a:
#        left, right = edges
#        graph[right] += [left]
#    while len(sort) < n:
#        for i in range(n):
#            loop = True
#            if graph[i] == []:
#                loop = False
#                del graph[i]
#                sort.append(i)
#                for edge in graph:
#                    try:
#                        graph[edge].remove(i)
#                    except:
#                        pass
#        if loop == True:
#            return None
#    return sort
#

if __name__ == "__main__":
    print order(8, [(5, 7), (5, 6), (4, 5), (3, 5), (3, 4), (2, 4), (2, 3), (1, 2), (0, 2)])
    print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
    print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
    print order(8, [(5, 7), (5, 6), (4, 5), (3, 5), (4, 3), (2, 4), (2, 3), (1, 2), (0, 2)])
    print order(4, [(0,1), (1,2), (2,1), (2,3)])

    print order2(8, [(5, 7), (5, 6), (4, 5), (3, 5), (3, 4), (2, 4), (2, 3), (1, 2), (0, 2)])
    print order2(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
    print order2(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
    print order2(8, [(5, 7), (5, 6), (4, 5), (3, 5), (4, 3), (2, 4), (2, 3), (1, 2), (0, 2)])
    print order2(4, [(0,1), (1,2), (2,1), (2,3)])
