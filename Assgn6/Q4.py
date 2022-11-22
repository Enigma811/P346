import re
from mypylib import mat_iter as mi
from mypylib import de as de


# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn6\Q4 in.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

# mi.prm(in_mat)
# ini_v=[[1],[1],[1]]
ini_v=0
eval,evec=de.pow_iter_eval(in_mat,0.001,ini_v)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn6\Q4 out.txt", "w+")
fout.writelines("Eigenvalue estimation by Power iteration (Precision: 10^-3)\n\n")
fout.close()

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn6\Q4 out.txt", "a")
fout.writelines("\nInput matrix:\n")
for i in range(len(in_mat)): 
    for j in range(len(in_mat)):fout.writelines(str(in_mat[i][j])+" ")
    fout.writelines("\n")
fout.writelines("\nThe dominant eigenvalue is "+str(eval[1]))
fout.writelines("\nThe corresponding eigenvector is:\n")
for i in range(len(evec)):fout.writelines(str(evec[i][0])+"\n")
fout.writelines("\nThe number of iterations taken to obtain given precision = "+str(eval[0])+"\n")
fout.writelines("\nThe initial test vector is: "+str(eval[2]))
fout.close()