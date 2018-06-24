from collections import OrderedDict
n = int(input())
duplicated = []

for i in range(0,n): duplicated.append(input())
  
wordlist = list(OrderedDict.fromkeys(duplicated))
print(len(wordlist))

for word in wordlist:
  print(duplicated.count(word),end= " ")