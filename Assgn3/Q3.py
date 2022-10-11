import re
from mypylib import random as rn
from mypylib import mat_iter as mi

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 in.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

#breaking the augmented matrix
if len(in_mat)+1 == len(in_mat[0]):
    #extracting A & B
    A = [0]*len(in_mat)
    B = [0]*len(in_mat)
    for k in range(0, len(in_mat)): A[k] = [0]*len(in_mat)
    for i in range(0, len(in_mat)):
        B[i] = in_mat[i][(len(in_mat[0])-1)]
        for j in range(0, len(in_mat)): A[i][j] = in_mat[i][j]
    

    # doolittle LU Decomposition
    t = mi.doolittle_lu(A)

    l = [0]*len(t)
    u = [0]*len(t)
    for j in range(0, len(t)): #creating l and u
        l[j] = [0]*len(t)
        u[j] = [0]*len(t)
    for i in range(0, len(t)):
        for j in range(0, len(t)):
            if i==j:
                l[i][i] = 1
                u[i][i] = t[i][i]
            elif i>j: l[i][j] = t[i][j]
            else: u[i][j] = t[i][j]

    #forward substitution
    for i in range(0, len(l)):
        sum = 0
        for j in range(0,i): sum = sum + (l[i][j]*B[j])
        B[i] = (B[i] - sum)/l[i][i]
    
    #backward substitution
    for i in range(len(u)-1,-1,-1):
        sum2 = 0
        for j in range(i+1, len(u)): sum2 += u[i][j]*B[j]
        B[i] = (B[i] - sum2)/u[i][i]
    
    #file print module
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 out.txt", "w")
    fout.writelines("\nSolution by doolittle_LU decomposition\n" +"Solution: "+str(B)+"\n")
    fout.close()
    
    

    #Gauss-Seidel
    res = mi.gsd(mi.diag_dom(in_mat),0.000001,500,1)
    #file print module
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 out.txt", "a")
    fout.writelines("\nSolution by Gauss Seidel (Precision: 10^-6)\n"+"Number of iterations: " + str(res[len(res)-1])+"\nSolution: ")
    res.remove(res[len(res)-1])
    fout.writelines(str(res)+"\n")



    #Gauss-Jacobi
    res = mi.gji(mi.diag_dom(in_mat),0.000001,500,1)
    #file print module
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 out.txt", "a")
    fout.writelines("\nSolution by Gauss Jacobi (Precision: 10^-6)\n"+"Number of iterations: " + str(res[len(res)-1])+"\nSolution: ")
    res.remove(res[len(res)-1])
    fout.writelines(str(res)+"\n")

else:
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn3\Q3 out.txt", "w")
    fout.writelines("\nError: Invalid input\n\nEnter augmented matrix A|B where AX=B\n")
    fout.close()
