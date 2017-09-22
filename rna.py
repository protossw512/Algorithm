# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 20:18:45 2016

@author: hello
"""
from collections import defaultdict
from heapq import heappush, heappop, heapify
from random import randint

#test whether an element can be paired with another
def pair(s):
    """
    Find the pair
    """
    pairs = {'A': 'U', 'U': 'AG', 'G': 'CU', 'C': 'G'}
    return pairs[s]

#solution for question 1
def best(a):
    back = defaultdict(lambda: -1)
    n = len(a)
    def _best(i, j, opt=defaultdict(int)):
        if (i, j) in opt:
            return opt[i, j]
        if i + 1 < j:
            if a[j -1] in pair(a[i]):
                ans = 1 + _best(i + 1, j - 1)
                back[i, j] = [[i, j]]
            else:
                ans = 0
            for k in range(i + 1, j):
                if _best(i, k) + _best(k, j) > ans:
                    ans = _best(i, k) + _best(k, j)
                    back[i, j] = [[i, k], [k, j]]
            opt[i, j] = ans
        return opt[i, j]
    return _best(0, n), solution(0, n, back, a)

def solution(i, j, back, a):
    sol = ['.'] * len(a)
    def _solution(i, j, back):
        if (i, j) not in back:
            return
        if len(back[i, j]) == 1:
            sol[i] = '('
            sol[j - 1] = ')'
            _solution(i + 1, j - 1, back)
            return
        else:
            k = back[i, j][1][0]
            _solution(i, k, back)
            _solution(k, j, back)
            return
    _solution(i, j, back)
    return ''.join(sol)

#solution for question 2
def total(a):
    n = len(a)
    def _best(i, j, opt=defaultdict(lambda: 1)):
        if (i, j) in opt:
            return opt[i, j]
        if i + 1 < j:
            opt[i, j] = _best(i+1, j)
            for k in range(i + 1, j + 1):
                if a[k -1] in pair(a[i]):
                    opt[i, j] += _best(i + 1, k - 1)* _best(k, j)
        return opt[i, j]
    return _best(0, n)

#modified quick select for question 3
def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0], a[pindex] = a[pindex], a[0]
        pivot = a[0]
        left = [x for x in a if x[0] < pivot[0]]
        right = [x for x in a[1:] if x[0] >= pivot[0]]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            qselect(k-lleft-1, right)

#solution for question 3 with extra credict [1] [2] [3]
def kbest(b, k):
    back = defaultdict(lambda: -1)  #back trace pointer
    def _kbest(i, j, opt=defaultdict(list)):
        def trypush(split, p, q):
            if p < len(_kbest(i + 1, split - 1)) and q < len(_kbest(split, j)) \
               and (split, p, q) not in used:
                used.add((split, p, q))
                heappush(heap, (-_kbest(i + 1, split - 1)[p]\
                                - _kbest(split, j)[q] - 1, split, p, q))

        def trypush1(p):
            if p < len(_kbest(i + 1, j)):
                heappush(heap, (-_kbest(i + 1, j)[p], p))

        if (i, j) in opt:
            return opt[i, j]
        if i == j:
            opt[i, j] = [0]
        elif i + 1 == j:
            opt[i, j] = [0]
        elif i + 1 < j:
            heap, used = [], set()
            temp = []
            temp.append((-_kbest(i + 1, j)[0], 0))
            #Initialize the heap, we put all first element from different edges in temp
            for split in xrange(i + 1, j + 1):
                if b[split -1] in pair(b[i]):
                    temp.append((-_kbest(i + 1, split - 1)[0]\
                                 - _kbest(split, j)[0] - 1, split, 0, 0))
            #if temp <= k , which means the number of edges is larger than k,
            #heapify will be faster than quickselect
            if len(temp) <= k:
                heapify(temp)
                heap = temp
            else:
                #if temp > k, we can use quickselect to select top k edges and discard others
                for _ in range(k):
                    best = qselect(1, temp)
                    temp.remove(best)
                    heap.append(best)
            #pop k-best element in the heap
            for top in xrange(k):
                if heap != []:
                    h = heappop(heap)
                    if len(h) == 4: #the element we popped is from hyper edges
                        v, split, p, q = h
                        trypush(split, p + 1, q)
                        trypush(split, p, q + 1)
                        back[i, j, top] = [[i, split, p], [split, j, q]]
                    else: # the element we popped is from normal edge
                        v, p = h
                        trypush1(p + 1)
                        back[i, j, top] = [[i + 1, j, p]]
                    opt[i, j].append(-v)
        return opt[i, j]
    temp = _kbest(0, len(b))
    result = []
    for top in range(len(temp)):
        result.append((temp[top], kbsolution(0, len(b), top, back, b)))
    return result

#back tracing function
def kbsolution(i, j, top, back, a):
    sol = ['.'] * len(a)
    def _kbsolution(i, j, top, back):
        if (i, j, top) not in back:
            return
        if len(back[i, j, top]) == 1:
            x, y, z = back[i, j, top][0]
            _kbsolution(x, y, z, back)
            return
        else:
            split = back[i, j, top][1][0]
            sol[i] = '('
            sol[split - 1] = ')'
            _kbsolution(split, j, back[i, j, top][1][2], back)
            _kbsolution(i + 1, split - 1, back[i, j, top][0][2], back)
            return
    _kbsolution(i, j, top, back)
    return ''.join(sol)

#solution for question 3 with extra credict [1]
#def kbest(b, k):
#    back = defaultdict(lambda : -1)
#    def _kbest(i, j, opt=defaultdict(list)):
#        def trypush(split, p, q):
#            if p < len(_kbest(i + 1, split - 1)) and q < len(_kbest(split, j)) and (split, p, q) not in used:
#                used.add((split, p, q))
#                heappush(heap, (-_kbest(i + 1, split - 1)[p] - _kbest(split,j)[q] - 1, split, p, q))
#
#        def trypush1(p):
#            if p < len(_kbest(i + 1, j)):
#                heappush(heap, (-_kbest(i + 1, j)[p], p))
#
#        if (i, j) in opt:
#            return opt[i, j]
#        if i == j:
#            opt[i, j] = [0]
#        elif i + 1 == j:
#            opt[i, j] = [0]
#        elif i + 1 < j:
#            heap, used = [], set()
#            trypush1(0)
#            for split in xrange(i + 1, j + 1):
#                if b[split -1] in pair(b[i]):
#                    trypush(split, 0, 0)
#            for top in xrange(k):
#                if heap != []:
#                    h = heappop(heap)
#                    if len(h) == 4:
#                        v, split, p, q = h
#                        trypush(split, p + 1, q)
#                        trypush(split, p, q + 1)
#                        back[i, j, top] = [[i, split, p],[split, j, q]]
#                    else:
#                        v, p = h
#                        trypush1(p + 1)
#                        back[i, j, top] = [[i + 1, j, p]]
#                    opt[i, j].append(-v)
#        return opt[i, j]
#    temp = _kbest(0, len(b))
#    result = []
#    for top in range(len(temp)):
#        result.append((temp[top], kbsolution(0, len(b), top, back, b)))
#    return result
#    return _kbest(0, len(b)), back




if __name__ == '__main__':
#    print best('ACAGU')
#    print best('AC')
#    print best('GUAC')
#    print best('GCACG')
#    print best('CCGG')
#    print best('CCCGGG')
#    print best('UUCAGGA')
#    print best('AUAACCUA')
#    print best('AGGCAUCAAACCCUGCAUGGGAGCG')
#    print total('ACA')
#    print total('AUA')
#    print total('UAU')
#    print total('ACAGU')
#    print total('AC')
#    print total('GUAC')
#    print total('GCACG')
#    print total('CCGG')
#    print total('CCCGGG')
#    print total('UUCAGGA')
#    print total('AUAACCUA')
#    print total('UUGGACUUG')
#    print kbest('AU', 2)
#    print kbest('CAU', 3)
    print kbest('GAUGCCGUGUAGUCCAAAGACUUC', 10)
#    print kbest('CCCGGG', 10)
#    print kbest('AGGCAUCAAACCCUGCAUGGGAGCG', 10)
