from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import de as de
import math

f = "math.sqrt(1 + (1/x))"
df = "-1/(2*math.sqrt((x**3)*(x+1)))"
t = "0"


#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn5\Q1 out.txt", "w+")
fout.writelines("Numerical  Integration\n\n"+"Method              Result                N\n")
fout.close()

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn5\Q1 out.txt", "a")
for i in range(1,4):
    fout.writelines("Midpoint"+"        "+str(de.midpt_integ(f,t,1,4,(10*i)))+"         "+str(10*i)+"\n")
    fout.writelines("Trapezoidal"+"     "+str(de.trap_integ(f,t,1,4,(10*i)))+"         "+str(10*i)+"\n")
    fout.writelines("Simpson"+"         "+str(de.simp_integ(f,t,1,4,int(10*i)))+"         "+str(10*i)+"\n\n")
fout.close()

#plotting the convergence (extra)

x = []
y1 = []
y2 = []
y3 = []
leg = ["Midpt", "Trap", "Simp"]
for i in range(1, 4):
    x.append(10*i)
    y1.append(de.midpt_integ(f,t,1,4,(10*i)))
    y2.append(de.trap_integ(f,t,1,4,(10*i)))
    y3.append(de.simp_integ(f,t,1,4,int(10*i)))
fig, ax = plt.subplots()
plt.scatter(x,y1)
plt.scatter(x,y2)
plt.scatter(x,y3)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(leg,loc='upper center')
plt.xlabel("N")
plt.ylabel("Estimate of Integral")
plt.title("Q1: Numerical Integration - sqroot(1+1/x) (from 1 to 4)")
plt.savefig("Q1.png")
# plt.show()

