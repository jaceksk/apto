'''
zminimalizuj: x + y
przy ograniczeniach:
   y ≥ x -1
   y ≥ -4x + 4
   y ≤ -0.5x + 3
'''

from pulp import *
model = LpProblem( "test", LpMinimize)   # LpMaximize dla maksymalizowania funkcji celu

# default lowBound and upBound is infinity
x = LpVariable( "x" , cat = "Continuous")
y = LpVariable( "y" , cat = "Continuous")

# funkcja celu
model += x + y
# ograniczenia
model += y >= x-1
model += y >= -4*x + 4
model += y <= -0.5*x + 3

print(model)

'''
for GLPK need install glp-utils
ubuntu: sudo apt-get install glpk-utils
'''

model.solve(GLPK(msg =0))

if LpStatus[model.status] == "Optimal":
    for var in model.variables():
      print(var.name, "=", var.varValue)
    print(value(model.objective))
elif LpStatus[model.status] == "Unbounded":
    print(LpStatus[model.status])
else:
    print("Not found solve")