from dimacs import *
from itertools import *
from sys import *
from utils import *

def VC( VERTEX_LIST, k, S, n):
    # porażka (zabezpieczenie przed tym, że drugie wywołanie rekurencyjne może usunąć za dużo wierzchołków)
    if k < 0:
        return None 

    if not VERTEX_LIST:
        # jesli nie ma takiej krawedzi -> rozwiazanie znalezione
        return S 
    if k == 0:
        return None # nie ma rozwiązania
    
    v = getVertexLevelList(VERTEX_LIST, n)
    L = getVertexIfExistOneDegreeVertex(v)
    e = None

    if L:
        e = findVertexToPair(VERTEX_LIST, L)
    else:
        e = getMaxLevelVertex(v)
        
    S1 = VC(remove_edge(VERTEX_LIST, e), k-1, S + [e], n)

    return S1

def calculate(graphName):
    G = loadGraph("graph/" + graphName)
    VERTEX_LIST = edgeList( G )
    n = len(G)
    i = 1
    result = None
    offset = (int)(n/25)
    isPrint = 0

    print("Start", graphName, ", size:", n)

    while result is None:
        if i > isPrint:
            print("k: ", i)
            isPrint += offset
        result = VC(VERTEX_LIST, i, [], n)
        i+=1

    if result is not None and isVC( VERTEX_LIST, result):
        print("Graph ", graphName, " calculate, min CoverVertex is: ", len(result))
        saveSolution( "graph/" + graphName + ".sol", result)