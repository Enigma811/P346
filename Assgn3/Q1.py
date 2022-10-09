import re
from mypylib import random as rn
from mypylib import mat_iter as mi

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q1 in.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d+', s)]

if len(in_mat)+1 == len(in_mat[0]):
    A = [0]*len(in_mat)
    B = [0]*len(in_mat)
    for k in range(0, len(in_mat)): A[k] = [0]*len(in_mat)
    for i in range(0, len(in_mat)):
        B[i] = in_mat[i][(len(in_mat[0])-1)]
        for j in range(0, len(in_mat)): A[i][j] = in_mat[i][j]

    # Gauss-Jordan Elimination
    test = in_mat
    mi.gj_ele(test)
    out = [0]*len(test)
    for i in range(0, len(test)): out[i] = test[i][(len(test[0])-1)]

    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q1 out.txt", "w")
    fout.writelines("\nSolution by Gauss-Jordan Elimination\n" +"Solution: "+str(out)+"\n")
    fout.close()




    # doolittle LU Decomposition

    
else:
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 out.txt", "a")
    fout.writelines("\nError: Invalid input\n\nEnter augmented matrix A|B where AX=B\n")
    fout.close()