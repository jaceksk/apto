import os

# from zad1 import calculate
# from zad2 import calculate
# from zad1_3 import calculate
# from 1_zad4 import calculate
# from zad2_1 import calculate
# from zad2_2 import calculate
from zad4_1 import calculate
import time

calculateList = ["e5"]

def runFromLs():
    with os.popen('ls graph/') as pipe:
        dane = open('time', 'a')
        suffix = ".sol"
        fileNameList = [x.strip() for x in pipe]
        print(fileNameList)
        for line in fileNameList:
                if not line.endswith(suffix): # and line + ".sol" not in fileNameList:
                    try:
                        t1_start = time.process_time()
                        calculate(line)
                        t1_stop = time.process_time()
                        print("Graph ", line, " time during:", t1_stop - t1_start, "sec")
                        print("Graph ", line, " time during:", t1_stop - t1_start, "sec", file=dane)
                    except Exception as err:
                        print("error: {0}".format(err))
                        t1_stop = time.process_time()
                        print("Error while calculation ", line, " time during:", t1_stop - t1_start, "sec")
        dane.close()

def runFromList():
    for fileName in calculateList:
        calculate(fileName)



runFromLs()