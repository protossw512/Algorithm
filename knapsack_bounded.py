
import sys
import time
import random

def best(w, a):
    opt = {}
    back = {}
    n = len(a)
    for k in range (0,n + 1):
        opt[0,k]=0
        k += 1
    for k in range (0,w + 1):
        opt[k,-1]=0
        k += 1   
    def find(x, i, opt):
        if i == 0:
            opt[x, i] = 0
            return opt[x, i]
        if (x, i) in opt:
            return opt[x, i]
        else:
            maxi = {}
            for j in range (0, a[i - 1][2] + 1):
                if x >= a[i - 1][0] * j:
                    maxi[j] = (find(x - a[i - 1][0] * j, i - 1, opt) + a[i - 1][1]*j)
                j += 1
            opt[x, i] = max(maxi.values())
            if opt[x, i] != opt[x, i - 1]:
                back[x, i] = max(maxi, key=lambda k: maxi[k])
        return opt[x, i]
    for i in range(0, n + 1):
        find(w, i, opt)
        i += 1
    def traceback(w):
        solution = n * [0]
        b = n
        while b >= 1:
            if (w, b) in back:
                solution[b - 1] = back[w, b]
                w = w - a[b - 1][0] * back[w, b]
            b -= 1
        return solution
    return find(w, n, opt), traceback(w)

def best2(w, a):
    opt = {}
    back = {}
    n = len(a)
    for k in range (0,n + 1):
        opt[0,k] = 0
        k += 1
    for k in range (0,w + 1):
        opt[k,-1] = 0
        opt[k, 0] = 0
        k += 1

    for i in range(1, n + 1):
        maxi = {}
        for x in range(0, w + 1):
            for j in range(1, a[i - 1][2] + 1):
                if x >= a[i - 1][0]*j:
                    maxi[j] = (opt[x - a[i - 1][0]*j, i - 1] + a[i - 1][1] * j)
                j += 1
            if maxi != {}:
                opt[x, i] = max(maxi.values())
            else:
                opt[x, i] = opt[x, i - 1]
            if opt[x, i] != opt[x, i - 1]:
                back[x, i] = max(maxi, key = lambda k: maxi[k])
            x= x + 1
        i = i + 1
                
        
    def traceback(w):
        solution = n * [0]
        b = n
        while b >= 1:
            if (w, b) in back:
                solution[b - 1] = back[w, b]
                w = w - a[b - 1][0] * back[w, b]
            b -= 1
        return solution
    return opt[w, n], traceback(w)

if __name__ == "__main__":
    print best(3, [(2, 4, 2), (3, 5, 3)])
    print best(3, [(1, 5, 2), (1, 5, 3)])
    print best(3, [(1, 5, 1), (1, 5, 3)])
    print best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
    print best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])
    print best(5, [(1, 5, 3), (1, 5, 3),(1, 5, 3)])
    print best(5, [(1, 5, 3), (1, 5, 3)])
    print "\n"
    print best2(3, [(2, 4, 2), (3, 5, 3)])
    print best2(3, [(1, 5, 2), (1, 5, 3)])
    print best2(3, [(1, 5, 1), (1, 5, 3)])
    print best2(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
    print best2(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])
    print best2(5, [(1, 5, 3), (1, 5, 3),(1, 5, 3)])
    print best2(5, [(1, 5, 3), (1, 5, 3)])
#    random.seed(128)
#    sys.setrecursionlimit(15000)
#    n = 10
#    for _ in xrange(20):
#        lst = []
#        for _ in range(n):
#            lst.append((random.randint(1, 10), random.randint(1, 10),random.randint(1, 10))) 
#        starttime = time.time()
#        result = best(n, lst)
#        print n, time.time()-starttime
#        n *= 2