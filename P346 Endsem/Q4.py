from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import de as de
import math

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q4 in.txt", "r+")
inp = fin.readlines()


f = "1/(math.sqrt(1 - (float((math.sin((math.pi)/8))**2)*float((math.sin(x))**2))))"
t = "0"
r = de.simp_integ(f,t,0,((math.pi)/2),int(inp[0]))
res = 4*((1/9.8)**0.5)*r
# print(wer)

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q4 out.txt", "w+")
fout.writelines("Numerical  Integration (Simpson's Method): Pendulum's period of oscillation\n\n")
fout.close()

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q4 out.txt", "a")
fout.writelines("Precision = 10^-2\n\n")
fout.writelines("Number of divisions given = "+str(inp[0])+"\n\n")
fout.writelines("Length of pendulum = 1 m\n")
fout.writelines("Angular amplitude = pi/4\n")
fout.writelines("g = 9.8 m/s^2\n\n")
fout.writelines("Time period of oscillation = "+str(float(f'{res:.3f}'))+" s\n")
fout.close()
