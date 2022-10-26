from cProfile import label
import math

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import root_fit as rf

g = "math.log(x/2) - math.sin(2.5*x)"

res1 = rf.bisec(g,0.000001, 0.000001,1.5,2.5,1)
res2 = rf.regfal(g,0.000001, 0.000001,1.5,2.5,1)

res3 = rf.bisec(g,0.000001, 0.000001,1,4,1)
res4 = rf.regfal(g,0.000001, 0.000001,1,4,1)

res5 = rf.bisec(g,0.000001, 0.000001,3,4,1)
res6 = rf.regfal(g,0.000001, 0.000001,3,4,1)


#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q1 out.txt", "w")
fout.writelines("Root(s) of nonlinear function (Tolerance 10^-6)\n\n" +"\nf(x) = log(x/2) - sin(5x/2)\n\n"+"Method         Result     No. of iterations\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q1 out.txt", "a")
fout.writelines("\nIntial Bracket: (1.5,2.5)\n\n")
for i in range(1, len(res1)): fout.writelines("Bisection :     "+str(float(f'{res1[i][0]:.7f}'))+"   "+str(float(f'{res1[i][1]:.6f}'))+"\n")
fout.writelines("\n")
for i in range(1, len(res2)): fout.writelines("Regula falsi:   "+str(float(f'{res2[i][0]:.7f}'))+"   "+str(float(f'{res2[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Bracket: (1,4)\n\n")
for i in range(1, len(res3)): fout.writelines("Bisection :     "+str(float(f'{res3[i][0]:.7f}'))+"   "+str(float(f'{res3[i][1]:.6f}'))+"\n")
fout.writelines("\n")
for i in range(1, len(res4)): fout.writelines("Regula falsi:   "+str(float(f'{res4[i][0]:.7f}'))+"   "+str(float(f'{res4[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Bracket: (3,4)\n\n")
for i in range(1, len(res5)): fout.writelines("Bisection :     "+str(float(f'{res5[i][0]:.7f}'))+"   "+str(float(f'{res5[i][1]:.6f}'))+"\n")
fout.writelines("\n")
for i in range(1, len(res6)): fout.writelines("Regula falsi:   "+str(float(f'{res6[i][0]:.7f}'))+"   "+str(float(f'{res6[i][1]:.6f}'))+"\n")
fout.writelines("\n\nTherefore, Regula falsi converges to the root faster.")
fout.writelines("\nThe function has multiple roots.")
fout.close()

#plotting the convergence (extra)

x1 = []
y1 = []
x2 = []
y2 = []
for i in range(1, max(len(res1),len(res2))):
    if i < len(res2):
        x2.append(res2[i][1])
        y2.append(res2[i][0])
    x1.append(res1[i][1])
    y1.append(res1[i][0])
fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Bisection','Regula fal'),loc='upper center')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q1: Roots of Non-linear fn - Bracket (1.5,2.5)")
plt.savefig("Q1 Bracket 1.5,2.5.png")

x1 = []
y1 = []
x2 = []
y2 = []
for i in range(1, max(len(res3),len(res4))):
    if i < len(res4):
        x2.append(res4[i][1])
        y2.append(res4[i][0])
    x1.append(res3[i][1])
    y1.append(res3[i][0])
fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Bisection','Regula fal'),loc='upper center')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q1: Roots of Non-linear fn - Bracket (1,4)")
plt.savefig("Q1 Bracket 1,4.png")

x1 = []
y1 = []
x2 = []
y2 = []
for i in range(1, max(len(res5),len(res6))):
    if i < len(res6):
        x2.append(res6[i][1])
        y2.append(res6[i][0])
    x1.append(res5[i][1])
    y1.append(res5[i][0])
fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Bisection','Regula fal'),loc='upper center')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q1: Roots of Non-linear fn - Bracket (3,4)")
plt.savefig("Q1 Bracket 3,4.png")