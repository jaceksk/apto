import os

# from zad1 import calculate
# from zad2 import calculate
# from zad1_3 import calculate
# from 1_zad4 import calculate
from zad2_1 import calculate
from zad2_2 import calculate

calculateList = ['b100']

def runFromLs():
    with os.popen('ls graph/') as pipe:
        suffix = ".sol"
        fileNameList = [x.strip() for x in pipe]
        print(fileNameList)
        for line in fileNameList:
                if not line.endswith(suffix) and line + ".sol" not in fileNameList:
                        calculate(line)

def runFromList():
    for fileName in calculateList:
        calculate(fileName)

runFromLs()