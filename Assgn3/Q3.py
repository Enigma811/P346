import re
from mypylib import random as rn
from mypylib import mat_iter as mi

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 in.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d+', s)]

#breaking the augmented matrix
if len(in_mat)+1 == len(in_mat[0]):
    A = [0]*len(in_mat)
    B = [0]*len(in_mat)
    for k in range(0, len(in_mat)): A[k] = [0]*len(in_mat)
    for i in range(0, len(in_mat)):
        B[i] = in_mat[i][(len(in_mat[0])-1)]
        for j in range(0, len(in_mat)): A[i][j] = in_mat[i][j]
    
    #Cholesky

    a = mi.is_posdef(A)
    b = mi.is_sym(A)
    if a == True & b == True:
        A = mi.cholesky_deco(A)
        for i in range(0, len(A)):
            sum = 0
            for j in range(0,i): sum = sum + (A[i][j]*B[j])/A[i][i]
            B[i] = (B[i] - sum)/A[i][i]
    
    # fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q2 out.txt", "w")
    # fout.writelines("\nSolution by Cholesky decomposition\n" +"\nSolution: ")
    # fout.close()

    #Gauss-Seidel
    res = mi.gsd(in_mat,0.000001,50,1)
    #file print module
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 out.txt", "a")
    fout.writelines("\nSolution by Gauss Seidel\n"+"Number of iterations: " + str(res[len(res)-1])+"\nSolution: ")
    res.remove(res[len(res)-1])
    fout.writelines(str(res))

else:
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 out.txt", "a")
    fout.writelines("\nError: Invalid input\n\nEnter augmented matrix A|B where AX=B\n")
    fout.close()