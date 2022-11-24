from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

def SHO_RK4(f1,f2,x0,y10,y20,h,n=100):
# 'f1' - (dy1/dx) 
# 'f2' - (dy2/dx) or (d^2y1/dx^2)
# 'x0' - independent variable - initial value
# 'y10' - y1 - initial value
# 'y20' - y2 - initial value
# 'h' - step size of independent variable
# 'n' - max iteration count
    
    res = [[x0,y10]]
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
        res[(len(res)-1)].append(x0 + i*h)
        res[(len(res)-1)].append(y1n)
        # res[(len(res)-1)].append(y2n)
    
    return(res)

# file read module
fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn6\Q1 in.txt", "r+")
inp = fin.readlines()
for i in range(len(inp)-1): inp[i] = inp[i][:-1] #input functions

fn = inp[0]
gn = inp[1]
s=30

a = SHO_RK4(fn,gn,0,2,-1,0.05,2000) 

#plotting
x = []
y = []
for i in range(len(a)):
    x.append(a[i][0])
    y.append(a[i][1])

fig, ax = plt.subplots()
# plt.plot(x,y)
plt.scatter(x,y, marker='.', s=s)
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
# plt.legend(('\u03BB','=0.2','\u03C9','=1.2'),loc='upper right')
plt.xlabel("Time (t)")
plt.ylabel("Position (y(t))")
plt.title("Forced-damped SHO (2*d\N{SUPERSCRIPT TWO}y/dx\N{SUPERSCRIPT TWO} + \u03BB*dy/dt + 2*y = 2*cos(\u03C9t)): RK4")
plt.savefig("Q1 \u03BB=0.2, \u03C9=1.2.png")
# plt.show()