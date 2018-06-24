n = int(input())
for i in range(0,n):
  try:
      userinput = input().split()
      a = int(userinput[0])
      b = int(userinput[1])
      print(a//b)
  except ZeroDivisionError as e:
      print("Error Code: "+str(e))
  except ValueError as e:
      print("Error Code: "+str(e))
