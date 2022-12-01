from matplotlib.ticker import MultipleLocator
import numpy as np
import support as sup
from matplotlib import pyplot as plt


g = "2*(math.pi)*(x**3)*(math.exp(-(math.pi)*(x**2)))"

x = []
y = []
y_n = []
for j in range(300):
    y_j,x_j = sup.monte_carlo_uni(g,-4,4,(100*(j+1)),0)
    yn_j,xn_j = sup.monte_carlo_norm(g,-4,4,0,1,(100*(j+1)))
    x.append((100*(j+1)))
    y.append(x_j)
    y_n.append(xn_j)


fig, ax = plt.subplots()
# plt.scatter(x, y, marker='.', s=s)
plt.plot(x,y)
plt.plot(x,y_n)

ax.xaxis.set_major_locator(MultipleLocator(5000))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
leg = ["Uniform","Normal(0,1)"]
plt.legend(leg,loc='upper right')
plt.xlabel("N")
plt.ylabel("Variance")
plt.title("Example of Expectation (1st e.s.)")
plt.savefig("Example of Expectation (1st e.s.) 2.png")
# plt.show()
plt.close()