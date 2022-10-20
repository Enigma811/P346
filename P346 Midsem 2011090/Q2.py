import math
from os import truncate
import re
from mypylib import random as rn
from mypylib import mat_iter as mi
from mypylib import root_fit as rf

g = "(x-5)*math.exp(x) + 5"
h = "(x-4)*math.exp(x)"

a,b = rf.newraph(g,h,0.000001,0.000001,10)


wc = (6.626*3*(10**(-3)))/(a*1.381)

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q2 out.txt", "w")
fout.writelines("\nSolution by Newton Raphson (Precision: 10^-4)\n"+"\nWien's Constant: "+str(format(wc, '.4'))+"\nNumber of iterations: " + str(b))
fout.close()
