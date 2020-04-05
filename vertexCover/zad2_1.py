# algorytm 2-aproksymacyjny (wybieramy niepokrytą krawędź, dodajemy oba jej wierzchołki do rozwiązania)

from dimacs import *
from itertools import *
from sys import *
from utils import *

def VC( VERTEX_LIST):
    # G to graf wejściowy
    # S to zbiór wierzchołków, który budujemy
    # if [x for x in S if x == True]:
    S = []

    while VERTEX_LIST:
        #wybrana dowolna krawedz -> alternatywnie można zamiast 0 dać rand
        e = list(VERTEX_LIST)[0] 

        VERTEX_LIST = remove_edge(VERTEX_LIST, list(e)[0])
        VERTEX_LIST = remove_edge(VERTEX_LIST, list(e)[1])

        S += list(e)
    
    return S 



def calculate(graphName):
    G = loadGraph("graph/" + graphName)
    VERTEX_LIST = edgeList(G)

    print("Start", graphName, "Graph len: ", len(G))

    result = VC(VERTEX_LIST)

    if isVC( VERTEX_LIST, result):
        print("Result len: ", len(result))
        saveSolution( "graph/" + graphName + ".sol", result)
