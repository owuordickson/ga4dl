# -*- coding: utf-8 -*-
"""
@author: "Marziye Derakhshannia and Dickson Owuor"
@license: "MIT"
@version: "1.0"
@email: "dm.derakhshannia@gmail.com or owuordickson@gmail.com "
@created: "07 November 2020"

Description: genetic heuristic algorithm that optimizes data lake jobs

"""


import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import ga


# Sphere test function
def sphere(x):
    return sum(x**2)

# Problem definition
problem = structure()
problem.costfunc = sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10

# GA Parameters
params = structure()
params.maxit = 100
params.npop = 20
params.pc = 1
params.gamma = 0.1
params.mu = 0.1
params.sigma = 0.1

# Run GA
out = ga.run(problem, params)

# Results
# plt.plot(out.bestcost)
plt.semilogy(out.bestcost)
plt.xlim(0, params.maxit)
plt.xlabel('Iterations')
plt.ylabel('Best Cost')
plt.title('Genetic Algorithm (GA)')
plt.grid(True)
plt.show()
