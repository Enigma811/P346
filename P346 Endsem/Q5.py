from mypylib import root_fit as rf
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

def SRK4(f1,f2,x0,y10,y20,h,n=100):
# 'f1' - (dy1/dx) 
# 'f2' - (dy2/dx) or (d^2y1/dx^2)
# 'x0' - independent variable - initial value
# 'y10' - y1 - initial value
# 'y20' - y2 - initial value
# 'h' - step size of independent variable
# 'n' - max iteration count
    
    res = [[y10,y20]]
    x = x0
    xn = x0
    y1 = y10
    y1n = y10
    y2 = y20
    y2n = y20

    for i in range(1,n):
        x = x0 + (i-1)*h
        k1y1 = h*eval(f1)
        k1y2 = h*eval(f2)
        x = x + h/2
        y1 = y1n + (k1y1/2)
        y2 = y2n + (k1y2/2)
        k2y1 = h*eval(f1)
        k2y2 = h*eval(f2)
        y1 = y1n + (k2y1/2)
        y2 = y2n + (k2y2/2)
        k3y1 = h*eval(f1)
        k3y2 = h*eval(f2)
        y1 = y1n + (k2y1/2)
        y2 = y2n + (k2y2/2)
        x = x + h/2
        k4y1 = h*eval(f1)
        k4y2 = h*eval(f2)
        y1n = y1n + (k1y1 + 2*k2y1 + 2*k3y1 + k4y1)/6
        y2n = y2n + (k1y2 + 2*k2y2 + 2*k3y2 + k4y2)/6
        
        res.append([])
        # res[i] = res[i-1] + (h/6)*(t1 + 4*t2 + t3)
        # res[(len(res)-1)].append(x0 + i*h)
        res[(len(res)-1)].append(y1n)
        res[(len(res)-1)].append(y2n)
    
    return(res)

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q5 in.txt", "r+")
inp = fin.readlines()
for i in range(len(inp)-1): inp[i] = inp[i][:-1] #input functions

fn = inp[0]
gn = inp[1]
s=5

a = SRK4(fn,gn,0,0,10,0.001,2000) 

#finding maximum height
eom = "10*x - 5*(x**2)"
tof = rf.bisec(eom,0.0001,0.001,0.1,4)
x = tof[0]/2
h_max = float(f'{eval(eom):.2f}')
# print(h_max)

#plotting
x = []
y = []
z = []
zn = []
for i in range(len(a)):
    if a[i][0]<0:break
    x.append(a[i][0])
    y.append(a[i][1])
    z.append(h_max)

hn_max = 0
for i in range(len(x)):
    if x[i]>hn_max: hn_max=x[i]

for i in range(len(x)): zn.append(hn_max)

fig, ax = plt.subplots()
# plt.plot(x,y)
plt.scatter(x,y, marker='.', s=s)
plt.plot(z,y,'k--')
plt.plot(zn,y,'k-.')
# ax.xaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.ylabel("Velocity (v(t))")
plt.xlabel("Height (y(t))")
leg = ["v vs y (with drag)","Max ht w/o drag","Max ht w drag"]
plt.legend(leg,loc='upper center')
plt.title("1-D motion with drag (2*d\N{SUPERSCRIPT TWO}y/dt\N{SUPERSCRIPT TWO} + \u03B3*dy/dt = g): RK4")
plt.savefig("Q5 g=10, \u03B3=0.02.png")
# plt.show()

#file print module
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q5 out.txt", "w+")
fout.writelines("1-D motion with drag (d^2y/dt^2 + gamma*(dy/dt) = g): RK4\n\n")
fout.close()
fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q5 out.txt", "a")
fout.writelines("gamma = 0.02 s^(-1)\n")
fout.writelines("g = 10 m/s^2\n\n")
fout.writelines("Precision: 10^-3\n\n")
fout.writelines("Initial conditions:\n")
fout.writelines("y(0) = 0 m, v(0) = 10 m/s\n\n")
fout.writelines("Equation of motion without air resistance:\n")
fout.writelines("y(t) = u(t)*t - 0.5*g*t^2\n\n")
fout.writelines("Thus, time of flight (without air resistance) = 2 s       (for y=0 in eq. of motion)\n\n")
fout.writelines("Max height (without air resistance) = "+str(h_max)+" m       (attained at t=1, by symmetry)\n\n")
fout.writelines("Max height (with air resistance) = "+str(float(f'{hn_max:.4f}'))+" m\n\n")
fout.close()