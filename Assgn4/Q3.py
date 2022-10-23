import re
import numpy as np
from mypylib import root_fit as rf
from matplotlib import pyplot as plt

#input is the list of coefficients of the polynomial in ascending order of power.
a = [4,0,-5,0,1]
b = rf.lagu(a,0.000001,0.000001) #precision is taken to be 10^-6

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q3 out.txt", "w")
fout.writelines("\nRoot(s) of polynomial by Laguerre's method (Precision 10^-6)\n\n" +"\nRoot   No. of iterations\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q3 out.txt", "a")
for i in range(len(b)): fout.writelines(str(float(f'{b[i][0]:.6f}'))+"        "+str(b[i][1])+"\n")
fout.writelines("\nThe roots of "+str(rf.pr_poly(a))+" are ")
for i in range(len(b)):
    if i == len(b) - 1: fout.writelines(str(float(f'{b[i][0]:.6f}'))+"\n")
    else: fout.writelines(str(float(f'{b[i][0]:.6f}'))+", ")
fout.close()
