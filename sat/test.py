import pycosat
import random         
import PyGnuplot as g
from numpy import arange
from dimacs import saveCNF

# +/-
S = [1,-1]

# generowanie formul
def generateFormula(k, n, a):
    V = range(1,n+1)      # lista zmiennych 1...n
    cnf = []
    for i in range(int(a*n)):
        kl = []
        for j in range(k):
            x = random.choice(V)*random.choice(S) # losowo wybrana zmienna z losowym negowaniem
            kl += [x]
        cnf += [kl]
    return cnf
    

# k - liczba lieralow na klauzule
# n - liczba zmiennych
# T - liczbę powtórzeń 
# dx - krok a 
# a - przedzial do długości klauzul
def generate(k, n, T, a_start, a_end, dx):
    iter = arange (a_start, a_end + dx, dx)
    dane = open('dane', 'w') 
# Dla wartośći a z przedziału 1 do 10 (np. z krokiem 0.1)
    for a in iter:
#     Wygenerować T formuł zawierających po n zmiennych oraz a * n klauzul.
        sum = 0
        for t in range(1, T+1):
            cnf = generateFormula(k, n, a)
#     Dla każdej wygenerowanej formuły sprawdzić, czy jest spełnialna.
            if pycosat.solve(cnf) != 'UNSAT':
                sum+=1
#     Wypisać wartość a oraz iloraz S/T.
        print("T: " + str(t) + ", a: " +str(a) + ", sum: " + str(sum) + ", k: " + str(k) + ", S/T: " + str(sum/t))
        print(str(a) + " " + str(sum/T), file = dane) 

    dane.close() 

generate(3, 10, 100, 1, 20, 0.1)

# rysuj wykres z pliku dane
g.c('plot "dane" u 1:2')