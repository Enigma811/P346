import math
from matplotlib.ticker import MultipleLocator
import numpy as np
import support as sup
from matplotlib import pyplot as plt


g = "(x**4)*math.exp(0.25*(x**2))"

x = []
y = []
yn = []
for j in range(100):
    y_j = sup.mc_norm_prob(g,-2,2,0,1,(100*(j+1)))
    yn_j = sup.mc_norm_prob(g,-2,2,math.sqrt(8),1,(100*(j+1)))
    x.append((100*(j+1)))
    y.append(y_j)
    yn.append(yn_j)


fig, ax = plt.subplots()
# plt.scatter(x, y, marker='.', s=s)
plt.plot(x,y)
plt.plot(x,yn, color='orange')
leg = ["Normal(0,1)","Normal(sqrt(8),1)"]
plt.legend(leg,loc='lower right')
ax.xaxis.set_major_locator(MultipleLocator(5000))
ax.xaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.xlabel("N")
plt.ylabel("Estimate of probability")
plt.title("Example of Rarity")
plt.savefig("Example of Rarity.png")
# plt.show()
plt.close()