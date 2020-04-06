from dimacs import *
from itertools import *
from sys import *


#Calculate is VertexCover
def isVertexCover(min_Vertex, VERTEX_LIST):
    for V in VERTEX_LIST:
        if not list(V)[0] in min_Vertex and not list(V)[1] in min_Vertex:
            return False
    return True


def calculate(graphName):
    G = loadGraph("graph/" + graphName)
    VERTEX_LIST = edgeList( G )

    print("Start", graphName, "Graph len: ", len(G))

    class Found(Exception): pass
    try:
        for k in range(1, len(VERTEX_LIST)):
            for C in combinations(range(len(VERTEX_LIST)), k):
                if isVertexCover(C, VERTEX_LIST):
                    raise Found
    except Found:
        if isVC( VERTEX_LIST, C ):
            print("Result: ", C)
            saveSolution( "graph/" + graphName + ".sol", C )

calculate("e5")