import numpy as np 
import matplotlib.pyplot as plt 

minSalary = 20000
maxSalary = 80000
minAge = 21
maxAge = 65
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(minAge, maxAge, numberOfEntries)

plt.scatter(ages, salaries)

xaxis = np.array(range(1,101))
yaxis = xaxis * xaxis

plt.plot(xaxis, yaxis, color = "r")

plt.title("Plot")
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.legend()
plt.savefig("prettier_plot.png") # this must be before plt.show
plt.show()