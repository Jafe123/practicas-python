counter=0
if __name__ == "__main__":
   print("Prefiero ser módulo.")
else:
   print("Me gusta ser un módulo.")

import sys
 
for p in sys.path:
  print(p)
  
#otra forma
from sys import path
 
path.append('..∖∖modules')
 
import module
 
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
 
