#Q1
def myLCG(seed, n, scale = 32768, sgn = 1): # takes seed, the number of random numbers to be generated (n), the +-range (scale) in which the numbers are to be generated and 'sgn'.
# By default, scale = RANDMAX
# 'sgn' decides whether negative random numbers will be generated.
  random = [0] * n # blank array to store 'n' random numbers
  r = seed # the next random number
  a = 1103515245 # multiplier
  c = 12345 # increment
  m = 32768 # modulus: RANDMAX
  
  # b: base - decides whether negative random numbers will be generated, based on input 'sgn'
  # By default 'sgn' = 1; the function generates only positive random numbers within specified range
  # If 'sgn' is negative, negative numbers are generated
  if sgn >= 0: b = 0
  else: b = 1

  for i in range(n):
    r = (a*r + c)%m
    r = ((-1)**(b*(int(r))))*r
    r = (r*scale)/m
    random[i] = r
  del(r)
  del(a)
  del(c)
  del(m)
  del(b)
  return(random)

# Example of generated array of random numbers

fin = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn2\Q1 in.txt", "r+")
inp = fin.readlines()
ck = 0
if len(inp) in [2,3,4]:
  for i in range(len(inp)):
    if int(inp[i]): ck = 1
    else: ck = 0

if ck==1:
  fout = open(r"C:\Main\Study\Sem 5\P346 Computational Phy Lab\Code\Assgn2\Q1 out.txt", "w")
  out = myLCG(int(inp[0]),int(inp[1]),int(inp[2]),int(inp[3]))
  fout.writelines(str(out))
else: 
  print("Invalid inputs: the function takes 4 inputs")
  print("Seed: float, #ofnumbers: +ve integer, **scale: integer, **sgn: integer")
  print("** are optional args")