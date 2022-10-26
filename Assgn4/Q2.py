import math

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import root_fit as rf

g = "-x - math.cos(x)"
h = "-1 + math.sin(x)"

res1 = rf.bisec(g,0.000001, 0.000001,-1,1,1)
res2 = rf.regfal(g,0.000001, 0.000001,-1,1,1)

res3 = rf.bisec(g,0.000001, 0.000001,-3,-2,1)
res4 = rf.regfal(g,0.000001, 0.000001,-3,-2,1)

res5 = rf.bisec(g,0.000001, 0.000001,3,4,1)
res6 = rf.regfal(g,0.000001, 0.000001,3,4,1)

res7 = rf.newraph(g,h,0.000001,0.000001,0,1)
res8 = rf.newraph(g,h,0.000001,0.000001,-3,1)
res9 = rf.newraph(g,h,0.000001,0.000001,2,1)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q2 out.txt", "w")
fout.writelines("Root(s) of nonlinear function (Tolerance 10^-6)\n\n" +"\nf(x) = -x - cos(x)\n\n"+"Method         Result     No. of iterations\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn4\Q2 out.txt", "a")
fout.writelines("\nIntial Bracket: (-1,1)\n\n")
for i in range(1, len(res1)): fout.writelines("Bisection :     "+str(float(f'{res1[i][0]:.7f}'))+"   "+str(float(f'{res1[i][1]:.6f}'))+"\n")
fout.writelines("\n")
for i in range(1, len(res2)): fout.writelines("Regula falsi:   "+str(float(f'{res2[i][0]:.7f}'))+"   "+str(float(f'{res2[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Bracket: (-3,-2)\n\n")
for i in range(1, len(res3)): fout.writelines("Bisection :     "+str(float(f'{res3[i][0]:.7f}'))+"   "+str(float(f'{res3[i][1]:.6f}'))+"\n")
fout.writelines("\n")
for i in range(1, len(res4)): fout.writelines("Regula falsi:   "+str(float(f'{res4[i][0]:.7f}'))+"   "+str(float(f'{res4[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Bracket: (3,4)\n\n")
for i in range(1, len(res5)): fout.writelines("Bisection :     "+str(float(f'{res5[i][0]:.7f}'))+"   "+str(float(f'{res5[i][1]:.6f}'))+"\n")
fout.writelines("\n")
for i in range(1, len(res6)): fout.writelines("Regula falsi:   "+str(float(f'{res6[i][0]:.7f}'))+"   "+str(float(f'{res6[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Guess: 0\n\n")
for i in range(1, len(res7)): fout.writelines("Newton Raphson :     "+str(float(f'{res7[i][0]:.7f}'))+"   "+str(float(f'{res7[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Guess: -3\n\n")
for i in range(1, len(res8)): fout.writelines("Newton Raphson :     "+str(float(f'{res8[i][0]:.7f}'))+"   "+str(float(f'{res8[i][1]:.6f}'))+"\n")
fout.writelines("\n\nIntial Guess: 2\n\n")
for i in range(1, len(res9)): fout.writelines("Newton Raphson :     "+str(float(f'{res9[i][0]:.7f}'))+"   "+str(float(f'{res9[i][1]:.6f}'))+"\n")

fout.writelines("\n\nTherefore, Newton Raphson converges to the root the fastest.")
fout.close()

#plotting the convergence (extra)

x1 = []
y1 = []
x2 = []
y2 = []
x7 = []
y7 = []
x8 = []
y8 = []
x9 = []
y9 = []
for i in range(1, max(len(res1),len(res2),len(res7),len(res8),len(res9))):
    if i < len(res2):
        x2.append(res2[i][1])
        y2.append(res2[i][0])
    if i < len(res7):
        x7.append(res7[i][1])
        y7.append(res7[i][0])
    if i < len(res8):
        x8.append(res8[i][1])
        y8.append(res8[i][0])
    if i < len(res9):
        x9.append(res9[i][1])
        y9.append(res9[i][0])
    if i < len(res1):
        x1.append(res1[i][1])
        y1.append(res1[i][0])

fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k', x7,y7, 'k:', x8,y8, 'k*', x9,y9, 'k-')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Bisection  (-1,1)','Regula fal (-1,1)','NewRaph: 0','NewRaph: -3','NewRaph: 2'),loc='lower right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q2: Roots of Non-linear fn")
plt.savefig("Q2 all.png")

fig, ax = plt.subplots()
plt.plot(x7,y7, 'k:', x8,y8, 'k', x9,y9, 'k--')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('NewRaph: 0','NewRaph: -3','NewRaph: 2'),loc='lower right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q2: Roots of Non-linear fn - Newton Raphson")
plt.savefig("Q2 Newraph.png")

fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Bisection  (-1,1)','Regula fal (-1,1)'),loc='lower right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q2: Roots of Non-linear fn - Bracket (-1,1)")
plt.savefig("Q2 Bracket -1,1.png")

x1 = []
y1 = []
x2 = []
y2 = []

for i in range(1, max(len(res3),len(res4))):
    if i < len(res4):
        x2.append(res4[i][1])
        y2.append(res4[i][0])
    if i < len(res3):
        x1.append(res3[i][1])
        y1.append(res3[i][0])

fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Bisection  (-3,-2)','Regula fal (-3,-2)'),loc='upper right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q2: Roots of Non-linear fn - Bracket (-3,-2)")
plt.savefig("Q2 Bracket -3,-2.png")

x1 = []
y1 = []
x2 = []
y2 = []

for i in range(1, max(len(res5),len(res6))):
    if i < len(res6):
        x2.append(res6[i][1])
        y2.append(res6[i][0])
    if i < len(res5):
        x1.append(res5[i][1])
        y1.append(res5[i][0])

fig, ax = plt.subplots()
plt.plot(x1,y1, 'k--',x2,y2,'k')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.legend(('Bisection  (3,4)','Regula fal (3,4)'),loc='upper right')
plt.xlabel("Iteration Count")
plt.ylabel("Root estimate")
plt.title("Q2: Roots of Non-linear fn - Bracket (3,4)")
plt.savefig("Q2 Bracket 3,4.png")