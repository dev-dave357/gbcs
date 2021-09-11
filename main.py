import sys
import math
import random
import threading
import time
import re
from functools import reduce


welcometext = '''=======================
--- WELCOME TO GBCS ---

    Guillermo Byte 
   Compression Sytem

Made by John Guillermo
======================='''
print(welcometext)
inputtext = input('Please type your input.\n')
res = ''.join(format(ord(i), '08b') for i in inputtext)
print(res)
x = list(res)
place = -1
if x[place] == "0":
  print(res, " is even")
  #odd conversion algotrithm
elif x[place] == "1":
  print(res, " is odd")
  #even conversion algotrithm
else:
  print(res)
  #Error message

# #converting list to string
# listed = ''.join([str(elem) for elem in x])
  
# print(listed)

