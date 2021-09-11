import sys
import math
import random
import threading
import time
import re
from functools import reduce
inputtext = input('Please type your input.\n')
res = ''.join(format(ord(i), '08b') for i in inputtext)
print(res)
x = list(res)
if x[-1] == "0":
  print()
  #odd conversion algotrithm
elif x[-1] == "1":
  print()
  #even conversion algotrithm
else:
  print()
  #Error message

# #converting list to string
# listed = ''.join([str(elem) for elem in x])
  
# print(listed)
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



























#determining whether it is a decimal or a whole
i = 100
f = 1.23


print(isinstance(i, int))
# True

print(isinstance(i, float))
# False

print(isinstance(f, int))
# False

print(isinstance(f, float))
# True