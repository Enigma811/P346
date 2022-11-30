import math
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import random as rn

def pbox(Na, Nb, dt, n=10000):
    N = Na + Nb
    na = [Na]
    nb = [Nb]
    x = [0]
    for i in range(n):
        for j in range(Na):
            t = rn.myLCG(i+j,1)
            if t <= Na/N:
                Na = Na - 1
                Nb = Nb + 1
        for k in range(Nb):
            t = rn.myLCG(i+j,1)
            if t <= Nb/N:
                Nb = Nb - 1
                Na = Na + 1
        x.append((i+1)*dt)
        na.append(Na)
        nb.append(Nb)
    fig, ax = plt.subplots()
    plt.scatter(x,na)
    plt.scatter(x,nb)
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.xaxis.set_major_formatter('{x:.0f}')
    # plt.grid()
    plt.xlabel("Time")
    plt.ylabel("N")
    plt.show()
    print("")

pbox(5000,0,0.1,1000)