import math
import time
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from mypylib import random as rn
from mypylib import mat_iter as mi
from mypylib import root_fit as rf
import numpy as np
import scipy.stats as stats

def stat_mean1d(arr):
    if len(arr)==0: return
    else:
        avg = 0
        for i in range(len(arr)): avg+=arr[i]
        avg = avg/(len(arr))
        return avg

def stat_var1d(arr):
    t = []
    v = []
    n = []
    for i in range(len(arr)):
        t.append(arr[i])
        if i==0: m = t[i]
        else: m = (i*m + t[i])/(i+1)
        
        sum = 0
        if i != 0:
            for j in range(len(t)): sum += (t[j]-m)**2
            sum = sum/(len(arr)-1)
        v.append(sum)
        n.append(i+1)
    return v,n


def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

#Monte Carlo uniform
def monte_carlo_uni(f,a,b,n,s=0):
  # 'f' - function to be integrated
  # 'a' - lower limit of integration
  # 'b' - upper limit of integration
  # 's' - seed; default = 0 corresponds to random seed (from system time)
  # 'n' - max iteration count
    res = 0
    sig = 0
    sqsum = 0
    if s==0: s = int(time.time()%100) 
    for i in range(1,n+1):
        t = rn.myLCG(s,1)
        t = a + (b-a)*t
        x = t
        sqsum += (float(eval(f)))**2
        res += eval(f)
        sig = (sqsum/i) - ((res/i)**2)
    res = res*(b-a)/n
    return res, sig

#Monte Carlo normal
def monte_carlo_norm(f,a,b,m,std,n):
  # 'f' - function to be integrated
  # 'a' - lower limit of integration
  # 'b' - upper limit of integration
  # 'n' - max iteration count
    res = 0
    sig = 0
    sqsum = 0
    t = stats.truncnorm((a - m) / std, (b - m) / std, loc=m, scale=std).rvs(n)
    tn = stats.truncnorm((a - m) / std, (b - m) / std, loc=m, scale=std).pdf(t)
    # tn = stats.norm.pdf(inp,m,std)
    # t = tn.rvs(n)
    # tn = normal_dist(t,m,std)
    for i in range(n):
        x = t[i]
        sqsum += (float(eval(f)/(tn[i]*10)))**2
        res += eval(f)/(tn[i]*10)
        sig = (sqsum/(i+1)) - ((res/(i+1))**2)
    res = res*(b-a)/n
    return res, sig


#Counting probbabilities
def mc_norm_prob(f,a,b,m,std,n):
  # 'f' - function to be integrated
  # 'a' - lower limit of integration
  # 'b' - upper limit of integration
  # 'n' - max iteration count
    ct = 0
    tot = 0
    res = 0
    t = stats.truncnorm((a - m) / std, (b - m) / std, loc=m, scale=std).rvs(n)
    tn = stats.truncnorm((a - m) / std, (b - m) / std, loc=m, scale=std).pdf(t)
    for i in range(n):
        x = t[i]
        # sqsum += (float(eval(f)/(tn[i]*10)))**2
        if (eval(f)/(tn[i]*10)) >= 1: 
            ct += 1
            tot += 1
            # res += eval(f)/(tn[i]*10)
        else: tot += 1   
    # res = res*(b-a)/n
    res = ct/tot
    return res


