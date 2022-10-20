import math
import re
from mypylib import random as rn
from mypylib import mat_iter as mi
from mypylib import root_fit as rf
import matplotlib.pyplot as plt

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\msem_fit.txt", "r+")
inp = fin.readlines()
#creatig the input nested list for fitting
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]



#replacing y_i with log(y_i) for exponential law
f = "math.log(y)"
for k in range(0, len(inp)):
    # jp[k][0] = in_mat[k][0]
    y = in_mat[k][1]
    in_mat[k][1] = float(eval(f))

b,t = rf.lsqfit_linear1d(in_mat)

#replacing x_i with log(x_i) for power law
g = "math.log(x)"
for k in range(0, len(inp)):
    x = in_mat[k][0]
    in_mat[k][0] = float(eval(g))

w,v = rf.lsqfit_linear1d(in_mat)

#file print module 
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q4 out.txt", "w")
fout.writelines("Straight Line fitting by least square method\n\n" +"\nFor power law:\n"+"\na = "+str(math.exp(w[0][0]))+"     Error in estimate: "+str(w[0][1]))
fout.close()

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q4 out.txt", "a")
fout.writelines("\nb = "+str(w[1][0])+"     Error in estimate: "+str(w[1][1]))
fout.writelines("\nPearson's r^2 : "+str(v))

fout.writelines("\n\nFor exponential law:\n"+"\na = "+str(math.exp(b[0][0]))+"     Error in estimate: "+str(b[0][1]))
fout.writelines("\nb = "+str(b[1][0])+"     Error in estimate: "+str(b[1][1]))
fout.writelines("\nPearson's r^2 : "+str(t))

fout.writelines("\n\n Thus, power law model gives a better fit for given data")
