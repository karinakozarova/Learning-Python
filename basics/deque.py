from collections import deque
d = deque()


n = int(input())
for i in range(0,n):
  userinput = input().split()
  if userinput[0] == "append":
    d.append(int(userinput[1]))
  elif userinput[0] == "appendleft":
    d.appendleft(int(userinput[1]))
  elif userinput[0] == "pop":
    d.pop()
  elif userinput[0] == "popleft":
    d.popleft()
    
for i in range(0, len(d)):
  print(d[i],end= " ")