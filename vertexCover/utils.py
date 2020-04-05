from dimacs import *
from itertools import *
from sys import *

def remove_edge(VERTEX_LIST, e):
    D = VERTEX_LIST.copy()
    D = [x for x in D if e not in x ]
    return D

def remove_edges(VERTEX_LIST, edges):
    D = VERTEX_LIST.copy()
    for e in edges:
        D = [x for x in D if e not in x]
    return D

def findVertex(VERTEX_LIST, e):
    D = VERTEX_LIST.copy()
    D = [x for x in D if e in x]
    return D

def getVertexLevelList(VERTEX_LIST, n):
    S = [0] * n
    for v in VERTEX_LIST:
        S[list(v)[0]] += 1
        S[list(v)[1]] += 1
    return S

def getMaxLevelVertex(v):
    max = 0
    max_v = 0
    i = 0
    for x in v:
        if x > max:
            max = x
            max_v = i
        i+=1
    return max_v

def getVertexIfExistOneDegreeVertex(v):
    i = 0
    for x in v:
        if x == 1:
            return i
        i+=1
    return None

def findVertexToPair(VERTEX_LIST, e):
    L = [x[1] for x in VERTEX_LIST if x[0] == e]
    if not L:
        return [x[0] for x in VERTEX_LIST if x[1] == e][0]
    else:
        return L[0]