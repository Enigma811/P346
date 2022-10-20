import math
import re
from mypylib import random as rn
from mypylib import mat_iter as mi
from mypylib import root_fit as rf

def Ar_ellipse(a, b, seed, n = 10000):

  
  if (a <= 0) or (b<=0):
    print("Error: Invalid input for lengths of semi minor axis and semi major axis; enter positive values")
    return
  x = 0
  y = 0
  ins = 0
  tot = 0
#   t = max(a,b)
#   print(t) 
  for i in range(n):
    x = rn.myLCG(seed, a, -1)
    y = rn.myLCG(seed, b, -1)
    # print("x",x)
    # print("y",y)
    # print("")
    ck = ((x**2)/(a**2) + ((y**2)/(b**2)))
    if ck <= 1:
      ins = ins + 1
      tot = tot + 1
    else:
      tot = tot + 1
  del x
  del y
  del ck
  Ar = 8*(ins/tot)
  del ins
  del tot
  return Ar, n

c,d = Ar_ellipse(2,1,20)

fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Q1 out.txt", "w")
fout.writelines("Area of Ellipse (Precision: 10^-4)\n"+str(c)+"\nNumber of iterations: " + str(d))
fout.close()
