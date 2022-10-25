import math
from mypylib import root_fit as rf

g = "math.log(x/2) - math.sin(2.5*x)"

a1,a2 = rf.bisec(g,0.000001, 0.000001,1.5,2.5)
a3,a4 = rf.bisec(g,0.000001, 0.000001,1,3)
a5,a6 = rf.bisec(g,0.000001, 0.000001,3,4)
a7,a8 = rf.bisec(g,0.000001, 0.000001,1,4)

b1,b2 = rf.regfal(g,0.000001, 0.000001,1.5,2.5)
b3,b4 = rf.regfal(g,0.000001, 0.000001,1,3)
b5,b6 = rf.regfal(g,0.000001, 0.000001,3,4)
b7,b8 = rf.regfal(g,0.000001, 0.000001,1,4)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q1 out.txt", "w")
fout.writelines("Root(s) of nonlinear function (Tolerance 10^-6)\n\n" +"\nf(x) = log(x/2) - sin(5x/2)\n\n"+"Method           Result              No. of iterations\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q1 out.txt", "a")
fout.writelines("Bisection :     "+str(a1)+"   "+str(a2)+"               Intial Bracket: (1.5,2.5)\n")
fout.writelines("Bisection :     "+str(a3)+"   "+str(a4)+"               Intial Bracket: (1,3)\n")
fout.writelines("Bisection :     "+str(a7)+"   "+str(a8)+"               Intial Bracket: (1,4)\n")
fout.writelines("Bisection :     "+str(a5)+"   "+str(a6)+"               Intial Bracket: (3,4)\n\n")
fout.writelines("Regula falsi:   "+str(b1)+"   "+str(b2)+"               Intial Bracket: (1.5,2.5)\n")
fout.writelines("Regula falsi:   "+str(b3)+"   "+str(b4)+"               Intial Bracket: (1,3)\n")
fout.writelines("Regula falsi:   "+str(b7)+"   "+str(b8)+"               Intial Bracket: (1,4)\n")
fout.writelines("Regula falsi:   "+str(b5)+"   "+str(b6)+"               Intial Bracket: (3,4)\n")
fout.writelines("\nTherefore, Regula falsi converges to the root faster.")
fout.writelines("\nThe function has multiple roots.")
fout.close()