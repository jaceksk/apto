import pycosat
import random         
import PyGnuplot as g
from dimacs import *
from numpy import arange
from itertools import *
from sys import *
import os

# Oznaczenie zmiennych w README

def index( i, j, k):
    return i*k + j + 1

def getColor(i, k, number):
    return number - 1 - i*k

def createClauseForVertex(i, k, n):
    cnf = []
    # część 1 - (( xi,1 ∨ xi,2 ∨ … ∨ xi,k ))
    for j in range(k):
        cnf += [index(i, j, k)]


    # część 2 - ( -xi,1 ∨ -xi,2 ) ∧ ( -xi,1 ∨ -xi,3 ) ∧… 
    clause = []
    for j in range(k):
        for l in range(j+1, k):
            clause += [[-index(i, j, k), -index(i, l, k)]]

    clause += [cnf]
    return clause
        

def calculateForK(VERTEX_LIST, k, n):
    cnf = []

    for i in range(n):
        cnf += createClauseForVertex(i, k, n)

    for v in VERTEX_LIST:
        for j in range(k):
            cnf += [[-index(v[0], j, k), -index(v[1], j, k)]]
    return cnf

def test(VERTEX_LIST, colorList, k):
    for v in VERTEX_LIST:
        if getColor(v[0], k, colorList[v[0]]) == getColor(v[1], k, colorList[v[1]]):
            print("Not correct")
            break
    
    print("Test passed successful for %d color" % k)

def prettyPrint(result, k):
    i = 0
    for number in result:
        print("%d: %d" % (i, getColor(i, k, number)))
        i+=1

def calculate(graphName):
    G = loadGraph("graph/" + graphName)
    VERTEX_LIST = edgeList( G )
    n = len(G)

    print("Start", graphName, "Graph len: ", n)

    c = True
    cnf = []
    k = 1
    result = []


    print("Start calculte for color number:", end='')
    while c and n != len(result):
        print(" %d," % k, end='')
        k+=1
        cnf = calculateForK(VERTEX_LIST, k, n)
        result = pycosat.solve(cnf)
        c = result == 'UNSAT'
    
    print()
    
    # > 0 znaczy, że kolorujemy
    result = [x for x in result if x > 0]
    print(result)

    test(VERTEX_LIST, result, k)
    # prettyPrint(result, k)

    return [k, result]
    
def runFromLs():
    with os.popen('ls graph/') as pipe:
        suffix = ".col"
        fileNameList = [x.strip() for x in pipe]
        print(fileNameList)
        for line in fileNameList:
                if line.endswith(suffix):
                        dane = open('result.txt', 'a+') 
                        result = calculate(line)
                        print(line + ": " + str(result[0]) + ": " + str(result[1]), file = dane) 
                        dane.close() 

# calculate("1-FullIns_3.col")
runFromLs()