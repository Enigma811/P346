#Q3

import matplotlib.pyplot as plt
from mypylib import random as rn

def gen_ranwalk(n, origin = [0,0], ls = 0):
# Input: number of steps (n)
# Input: origin of random walk (origin); Default - (0,0)
# Input: max step length (ls); Default - 0 > the max step length is fixed for each simulation, as 2*sqrt(2)
# (ls): Non zero value for 'ls' leads to different max step length for each simulation

  import time
  t = time.localtime()
  ct = time.strftime("%H%M%S", t)
  ct = int(ct)

  if ct > n: 
    seed1 = ct%n
    seed2 = n - (ct%n)
  elif ct == n: 
    seed1 = int(n/3)
    seed2 = int(n/2)
  else: 
    seed1 = 0
    seed2 = (n%ct)

  if ls == 0: t = 1
  else: t = ct%5

  x = rn.myLCG(seed1, n, 2*t, -1)
  y = rn.myLCG(x[seed1], n, 2*t, -1)
  ran_arr = [0] * int(n+1)

  for l in range(n+1): ran_arr[l] = [0] * 2
  ran_arr[0][0] = origin[0]
  ran_arr[0][1] = origin[1]

  for i in range(1,n):
    ran_arr[i][0] = x[i]
    ran_arr[i][1] = y[i]
  del(x)
  del(y)
  return(ran_arr)

def plot_ranwalk(n, origin = [0,0], ls = 0):
# takes the same inputs as random_walk()

  val = gen_ranwalk(n, origin, ls)
  X = [0] * (n+1)
  Y = [0] * (n+1)

  for i in range(1, (n+1)):
    X[i] = val[i][0] + ((X[i-1]))
    Y[i] = val[i][1] + ((Y[i-1]))
  
  del(val)

  plt.plot(X,Y)
  plt.xlabel("")
  plt.ylabel("")
  a = "Random walk: " + str(n) + " steps"
  plt.title(a)
  A = 0, round(X[n],3)
  B = 0, round(Y[n],3)
  for xy in zip(A, B):                                       # <--
    plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--
  plt.grid()
  del a
  plt.plot(X,Y)
  r1 = "C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn2\Q3 out(plot_ranwalk - " + str(n) + ").png"
  plt.savefig(r1)
  plt.close()

  
def ranwalkdist(n, origin = [0,0], ls = 0):
# takes the same inputs as random_walk()

  val = gen_ranwalk(n, origin, ls)
  X = [0] * (n+1)
  Y = [0] * (n+1)

  for i in range(1, (n+1)):
    X[i] = val[i][0] + ((X[i-1]))
    Y[i] = val[i][1] + ((Y[i-1]))
  
  del(val)
  
  x = [0] * n
  y = [0] * n

  dist = 0
  sum = 0
  for i in range(n):
    dist = dist + ((((X[i+1] - X[i])**2)+((Y[i+1] - Y[i])**2))**(0.5))
    sum = sum + (((X[i+1] - X[i])**2)+((Y[i+1] - Y[i])**2))
    x[i] = int(i+1)
    y[i] = (sum/n)**(0.5)

  rms = (sum/n)**(0.5)
  disp = ((((X[n])**2)+((Y[n])**2))**(0.5))

  del sum
  del dist
  del X
  del Y

  s1 = "The rms distance covered(per step) after " + str(n) + " steps: " + str(rms)
  s2 = "The displacement after " + str(n) + " steps: " + str(disp)
  L = [s1, "\n", s2, "\n"]
  del s1
  del s2

  plt.plot(x,y)
  plt.xlabel("Number of steps 'n'")
  plt.ylabel("RMS Distance covered in n steps")
  plt.title("RMS Distance covered in random walk vs no. of steps")
  r2 = "C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn2\Q3 out(ranwalkdist - " + str(n) + ").png"
  plt.savefig(r2)
  plt.close()
  return(L)

fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn2\Q3 in.txt", "r+")
inp = fin.readlines()
ck = 0
if len(inp) in [1,2,3]:
  for i in range(len(inp)):
    if int(inp[i]): ck = 1
    else: ck = 0

if ck==1:

  if len(inp) == 1: 
    plot_ranwalk(int(inp[0]))
    out = ranwalkdist(int(inp[0]))

  elif len(inp) == 2: 
    plot_ranwalk(int(inp[0]),int(inp[1]))
    out = ranwalkdist(int(inp[0]),int(inp[1]))
  else:
    plot_ranwalk(int(inp[0]),int(inp[1]),int(inp[2]))
    out = ranwalkdist(int(inp[0]),int(inp[1]),int(inp[2]))

  s = "C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn2\Q3 out(ranwalkdist - " + str(int(inp[0])) + ").txt"
  fout = open(s, "w")
  fout.writelines(out)
else: 
  print("Invalid inputs: the function takes 3 inputs")
  print("#of_steps: +ve integer, **origin: two element array containing (x,y) co-ordinates, **fixed step length: 0 or 1")
  print("** are optional args")