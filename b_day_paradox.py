# some fun with birth-day paradox
# solution to ex.10.8 of think python book (p.98)
# -cem bozsahin

import random

def has_duplicates(l):   # simple version: find all duplicates and check
   return len(l) != len([x for x in l for y in l if x==y])

def b_day(N,M,S):  # N: number of birthdays M: iterations, S: seed
  random.seed(S)  # reinitialize random number generator
  c=0
  for i in range(0,M):
    xs=[]
    for j in range(0,N):
      xs.append(random.randint(1,366))
    if has_duplicates(xs): 
      c+=1

  print N, M, c, c/float(M)
