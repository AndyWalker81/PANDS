import numpy as np
import matplotlib.pyplot as plt 

# reference: https://realpython.com/python-histograms/

# set absolute values
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

#np.random.seed(1) # to make random numbers the same each time
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print (salaries)

#plt.title("Salaries")
#plt.xlabel()
plt.hist(salaries, orientation='horizontal')
plt.show()