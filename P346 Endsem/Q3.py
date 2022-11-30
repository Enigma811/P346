import math
import time
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import root_fit as rf
from mypylib import random as rn

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q3 in.txt", "r+")
inp = fin.readlines()

g = str(float(inp[0]))+"- x*math.exp(x)"
h = "(-1-x)*math.exp(x)"
t = rn.myLCG((time.time()%100),100)

res = rf.newraph(g,h,0.000001,0.000001,t,1)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q3 out.txt", "w")
fout.writelines("Max displacement (Newton Raphson) (Tolerance 10^-3)\n\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q3 out.txt", "a")
fout.writelines("Initial guess for Newton Raphson = Random\n\n")
fout.writelines("\nFor displacement x, force acting on the system is given by:\n"+"F(x) = F - x*exp(x)\n")
fout.writelines("\nF = 2.5 N\n\n")
fout.writelines("At max displacement, the net force on the system is zero. Thus, we have,\n\n")
fout.writelines("Max displacement of spring = "+str(float(f'{res[len(res)-1][0]:.3f}'))+" m\n")
fout.close()
