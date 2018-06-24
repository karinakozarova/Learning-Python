import re

for i in range(0, int(input())):
  try:
      re.compile(input())
      print("True")
  except re.error:
      print("False")