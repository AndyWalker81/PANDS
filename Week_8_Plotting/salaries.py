# salaries.py
# Author: Andy Walker

import numpy as np 

# set absolute values
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # to make random numbers the same each time
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

salariesPlus = salaries + 5000
print (salariesPlus)

salariesMult = salaries * 1.05
print (salariesMult)

newSalaries = salariesMult.astype(int)
print (newSalaries)