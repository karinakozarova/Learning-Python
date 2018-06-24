import math
import os
import random
import re
import sys

def solve(s):
  splitted = s.split()
  length = len(splitted)
  for i in range(0,length):
    splitted[i] = splitted[i].capitalize()  # or splitted[i] = str(splitted[i][0].upper()) + str(splitted[i][1:])
  s = " "
  return s.join(splitted)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
