#Q2
# Volume of positive octant of unit sphere by throwing method
# takes seed and number of trials as input

from mypylib import random as rn

def Vol_sphere_octant(seed, n):
  sample = rn.myLCG(seed, n, 1, -1)
  x = 0
  y = 0
  z = 0
  ins = 0
  tot = 0 
  for i in range(n-3):
    x = sample[i]
    y = sample[i+1]
    z = sample[i+2]
    ck = ((x*x) + (y*y) + (z*z))
    if ck <= 1.0000000000000000:
      ins = ins + 1
      tot = tot + 1
    else:
      tot = tot + 1
  del(sample)
  del x
  del y
  del z
  del ck
  Vol = (ins/tot)
  del ins
  del tot
  return Vol

fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn2\Q2 in.txt", "r+")
inp = fin.readlines()
ck = 0
if len(inp) == 2:
  for i in range(len(inp)):
    if int(inp[i]): ck = 1
    else: ck = 0

if ck==1:
  fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn2\Q2 out.txt", "w")
  out = Vol_sphere_octant(int(inp[0]),int(inp[1]))
  fout.writelines(str(out))
else: 
  print("Invalid inputs: the function takes 2 inputs")
  print("Seed: integer, #of_numbers_for_throwing_method: +ve integer")