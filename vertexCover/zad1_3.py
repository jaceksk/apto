from dimacs import *
from itertools import *
from sys import *
from utils import *


def VC( VERTEX_LIST, k, S):
    
    # porażka (zabezpieczenie przed tym, że drugie wywołanie rekurencyjne może usunąć za dużo wierzchołków)
    if k < 0:
        return None 

    if not VERTEX_LIST:
        # jesli nie ma takiej krawedzi -> rozwiazanie znalezione
        return S 
    if k == 0:
        return None # nie ma rozwiązania


    # wybrana dowolna krawedz o stopniu większym niż 1
    e = list(list(VERTEX_LIST)[0])[0]
    S1 = VC(remove_edge(VERTEX_LIST, e), k-1, S + [e])

    if S1:
        return S1
    else:
        N = findVertex(VERTEX_LIST, e)
        P = list(set([x[1] if not x == e else x[0] for x in N]))

        D = remove_edges(VERTEX_LIST, P)
        S2 = VC(D, k-len(N), S + P)
        return S2


def calculate(graphName):
    G = loadGraph("graph/" + graphName)
    VERTEX_LIST = edgeList( G )

    print("Start", graphName, "Graph len: ", len(G))
    i=1
    result = None
    while result is None:
        result = VC(VERTEX_LIST, i, [])
        i+=1

    if isVC( VERTEX_LIST, result):
        print("Result: ", len(result))
        saveSolution( "graph/" + graphName + ".sol", result)
