from dimacs import *
from itertools import *
from sys import *
from utils import *

def VC( VERTEX_LIST, k, S):

    # G to graf wejściowy, k liczba wierzchołków, które możemy użyć
    # S to zbiór wierzchołków, który budujemy
    # if [x for x in S if x == True]:
    if not VERTEX_LIST:
        # jesli nie ma takiej krawedzi
        #rozwiazanie znalezione
        return S 
    else:
        e = list(VERTEX_LIST)[0] #wybrana dowolna krawedz
    if k == 0:
        return None # nie ma rozwiązania

    S1 = VC(remove_edge(VERTEX_LIST, list(e)[0]), k-1, S + [list(e)[0]])

    if S1:
        return S1
    else:
        S2 = VC(remove_edge(VERTEX_LIST, list(e)[1]), k-1, S + [list(e)[1]])
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
        print("Result: ", result)
        saveSolution( "graph/" + graphName + ".sol", result)
