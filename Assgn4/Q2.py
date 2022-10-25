import math
from mypylib import root_fit as rf

g = "-x - math.cos(x)"
h = "-1 + math.sin(x)"

a1,a2 = rf.bisec(g,0.000001, 0.000001)
a3,a4 = rf.bisec(g,0.000001, 0.000001,-3,-2)
a5,a6 = rf.bisec(g,0.000001, 0.000001,3,4)

b1,b2 = rf.regfal(g,0.000001, 0.000001)
b3,b4 = rf.regfal(g,0.000001, 0.000001,-3,-2)
b5,b6 = rf.regfal(g,0.000001, 0.000001,3,4)

c1,c2 = rf.newraph(g,h,0.000001,0.000001)
c3,c4 = rf.newraph(g,h,0.000001,0.000001,-3)
c5,c6 = rf.newraph(g,h,0.000001,0.000001,2)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q2 out.txt", "w")
fout.writelines("Root(s) of nonlinear function (Tolerance 10^-6)\n\n" +"\nf(x) = -x - cos(x)\n\n"+"Method           Result              No. of iterations\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q2 out.txt", "a")
fout.writelines("Bisection :     "+str(a1)+"   "+str(a2)+"               Intial Bracket: (-1,1)\n")
fout.writelines("Bisection :     "+str(a3)+"   "+str(a4)+"               Intial Bracket: (-3,-2)\n")
fout.writelines("Bisection :     "+str(a5)+"   "+str(a6)+"               Intial Bracket: (3,4)\n\n")
fout.writelines("Regula falsi:   "+str(b1)+"   "+str(b2)+"               Intial Bracket: (-1,1)\n")
fout.writelines("Regula falsi:   "+str(b3)+"   "+str(b4)+"               Intial Bracket: (-3,-2)\n")
fout.writelines("Regula falsi:   "+str(b5)+"   "+str(b6)+"               Intial Bracket: (3,4)\n\n")
fout.writelines("Newton Raphson: "+str(c1)+"    "+str(c2)+"              Initial guess: 0\n")
fout.writelines("Newton Raphson: "+str(c3)+"    "+str(c4)+"              Initial guess: -3\n")
fout.writelines("Newton Raphson: "+str(c5)+"    "+str(c6)+"              Initial guess: 2\n")
fout.writelines("\nTherefore, Newton Raphson converges to the root the fastest.")
fout.close()
