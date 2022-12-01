from matplotlib.ticker import MultipleLocator
import numpy as np
import support as sup
from matplotlib import pyplot as plt


g = "x*(math.exp(-(math.pi)*(x**2)))"

x = []
y = []
err = []
for j in range(300):
    y_j,x_j = sup.monte_carlo_norm(g,-4,4,0,1,(100*(j+1)))
    x.append((100*(j+1)))
    y.append(y_j)
    err.append(x_j)


fig, ax = plt.subplots()
# plt.scatter(x, y, marker='.', s=s)
plt.plot(x,y)
ax.xaxis.set_major_locator(MultipleLocator(5000))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.xlabel("N")
plt.ylabel("Estimate of integral")
plt.title("Example of Expectation (gs) - Normal sampling(0,2)")
plt.savefig("Example of Expectation (gs) - Normal sampling(0,2) 1.png")
# plt.show()
plt.close()

fig, ax = plt.subplots()
plt.plot(x,err)
ax.xaxis.set_major_locator(MultipleLocator(5000))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.xlabel("N")
plt.ylabel("Variance")
plt.title("Example of Expectation (gs) - Normal sampling(0,2)")
del x
del y
del err
del x_j
del y_j
plt.savefig("Example of Expectation (gs) - Normal sampling(0,2) 2.png")