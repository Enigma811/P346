import re

from matplotlib.ticker import MultipleLocator
from mypylib import mat_iter as mi
from mypylib import root_fit as rf
from matplotlib import pyplot as plt
import numpy as np

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\esem4fit.txt", "r+")
inp = fin.readlines()
#creatig the input nested list for fitting
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    t = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', t)]

# in_mat.pop(0)
# mi.prm(in_mat)

res = rf.lsqfit_poly1d(in_mat, 4)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q7 out.txt", "w")
fout.writelines("\nPolynomial fitting by Least square method\n\n" +"\nBest "+str(4)+" degree polynomial fit:\n"+str(rf.pr_poly(res)))
fout.close()

rf.plot_polyfit(in_mat, 4) #plotting using fucntion definition

#plotting manually
x1 = []
y1 = []
s = 30
for i in range(len(in_mat)):
    x1.append(in_mat[i][0])
    y1.append(in_mat[i][1])

fig, ax = plt.subplots()
plt.scatter(x1, y1,  color= 'black',marker='.', s=s)
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
f = str(rf.pr_poly(res))
yf = []
for i in range(len(x1)):
    x = x1[i]
    yf.append(eval(f))
for i in range(len(res)): res[i] = float(f'{res[i]:.2f}')
plt.plot(x1,yf)
leg = ["Data","Best quartic poly_fit"]
plt.legend(leg,loc='upper center')
plt.title("Fit: "+str(rf.pr_poly(res)))
plt.savefig("Q7 plot (manual).png")