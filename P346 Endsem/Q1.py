import re
from mypylib import mat_iter as mi

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q1 in.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

if mi.det(in_mat)==0: #checking if the determinant exists
    print("")
else:
    A = in_mat
    res = [[]]
    for i in range(in_mat):
        for j in range(in_mat): res[i].append(0)
        res.append([])
    B=[]

    for i in range(len(A)):
        for j in  range(len(A)):
            B.append(0)
        B[i] = 1

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
    
    for k in range(len(A)): res[i][k]=B[k]

res = mi.trans(res)

print(res)
# #file print module
# fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q1 out.txt", "a")
# fout.writelines(res)

    
