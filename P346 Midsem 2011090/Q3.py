import re
from mypylib import mat_iter as mi

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\msem_gs.txt", "r+")
inp = fin.readlines()
in_mat=[1]*len(inp)
for k in range(0, len(inp)): 
    s = inp[k]
    in_mat[k] = [float(d) for d in re.findall(r'-?\d*\.?\d+', s)]

#making augmented matrix
in_mat.pop(0)
in_mat.pop(len(in_mat)-1)

for i in range(0,6): in_mat[i].append(in_mat[i+8][0])
for i in range(10):
    if len(in_mat) < 7: break
    else: in_mat.pop(len(in_mat)-1)


#input to main function    
if len(in_mat)+1 == len(in_mat[0]):
    #Gauss-Seidel
    res = mi.gsd(in_mat,0.000001,50,1)
    #file print module
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q3 out.txt", "w")
    fout.writelines("Solution by Gauss Seidel (Precision: 10^-6)\n"+"Number of iterations: " + str(res[len(res)-1])+"\nSolution: ")
    res.remove(res[len(res)-1])
    fout.writelines(str(res))

else:
    fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q3 out.txt", "w")
    fout.writelines("\nError: Invalid input\n\nEnter augmented matrix A|B where AX=B\n")
    fout.close()