import re
from mypylib import root_fit as rf

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\assign4fit.txt", "r+")
inp = fin.readlines()
#creatig the input nested list for fitting
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

in_mat.pop(0)
# mi.prm(in_mat)

res = rf.lsqfit_poly1d(in_mat, 3)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q4 out.txt", "w")
fout.writelines("\nPolynomial fitting by Least square method\n\n" +"\nBest "+str(3)+" degree polynomial fit:\n"+str(rf.pr_poly(res)))
fout.close()

rf.plot_polyfit(in_mat, 3) #can be plotted manually with desired formatting as done for fucntion definition
