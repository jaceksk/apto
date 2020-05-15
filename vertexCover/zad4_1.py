'''
xi = 0 - wierzchołek v1 nie nalezy do pokrycia
xi = 1 - wierzchołek v1 nalezy do pokrycia

x1+x2+ ... + xn - minimum
'''

from pulp import *

from vertexCover.dimacs import loadGraph, edgeList, isVC, saveSolution

withWeight = True
isContinuesWeight = True
typeVariable = None

if withWeight:
    if isContinuesWeight:
        typeVariable = "Continues"
    else:
        typeVariable = "Integer"
else:
    typeVariable = "Binary"


def calculate(graphName):
    model = LpProblem("vertexCover", LpMinimize)
    G = loadGraph("graph/" + graphName)
    VERTEX_LIST = edgeList(G)

    print("Start", graphName, "Graph len: ", len(G), " type ", typeVariable)

    vars = [LpVariable(str(i), lowBound = 0, upBound = len(G)+10, cat = typeVariable) for i in range(len(G))]

    if withWeight:
        if isContinuesWeight:
            n = len(vars)
            weight = [i/n * vars[i] for i in range(len(vars))]
            model += sum(weight)
        else:
            weight = [i*vars[i] for i in range(len(vars))]
            model += sum(weight)
    else:
        model += sum(vars)

    for v in VERTEX_LIST:
        model += vars[v[0]] + vars[v[1]] >= 1

    # LpSolverDefault.msg = 1
    model.solve()

    if LpStatus[model.status] == "Optimal":
        result = [int(x.name) for x in model.variables() if x.varValue == 1.0]
        if isVC( VERTEX_LIST, result):
            print("Result graph ", graphName, " len: ", len(result))
            # saveSolution( "graph/" + graphName + ".sol", result)
        else:
            print("Bad result")
    elif LpStatus[model.status] == "Unbounded":
        print(LpStatus[model.status])
    else:
        print("Not found solve")
