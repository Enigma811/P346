from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import de as de

g = "(math.sin(x))**2"
s = 40
x = []
y = []
err = []
for j in range(300):
    y_j,x_j = de.monte_carlo_uni(g,-1,1,(100*(j+1)),10)
    x.append((100*(j+1)))
    y.append(y_j)
    err.append(x_j)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn5\Q2 out.txt", "w+")
fout.writelines("Numerical Integration by Monte Carlo (uniform sampling)(Precision: 10^-4)\n\n"+"N            Result         Error\n")
fout.close()

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn5\Q2 out.txt", "a")
for i in range(1,7): fout.writelines(str(x[(50*i)-1])+"        "+str(float(f'{y[(50*i)-1]:.5f}'))+"         "+str(float(f'{err[(50*i)-1]:.5f}'))+"\n")
fout.writelines("\nThe estimate for integral using "+str(x[(len(x)-1)])+" test points is "+str(float(f'{y[(len(y)-1)]:.5f}'))+" with an error of "+str(float(f'{err[(len(err)-1)]:.5f}'))+"\n")
fout.close()

#plotting the convergence (extra)

fig, ax = plt.subplots()
plt.scatter(x, y, marker='.', s=s)
ax.xaxis.set_major_locator(MultipleLocator(5000))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.xlabel("N")
plt.ylabel("Estimate of Integral")
plt.title("Q2: Monte Carlo Integration - (sin(x))^2 (from -1 to 1)")
del x
del y
del err
del s
del x_j
del y_j
plt.savefig("Q2.png")
# plt.show()