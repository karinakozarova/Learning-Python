#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N % 2 == 1:
      print("Weird")
    elif N > 20:
      print("Not Weird")
    elif N > 6:
      print("Weird")
    else:
      print("Not Weird")

    """
    If is odd, print Weird
    If is even and in the inclusive range of to , print Not Weird
    If is even and in the inclusive range of to , print Weird
    If is even and greater than , print Not Weird
"""
