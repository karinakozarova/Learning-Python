from collections import OrderedDict

n = int(input())
wordlist = []
for i in range(0,n):
  wordlist.append(input())
  
duplicated = wordlist

print(len(set(wordlist)))
wordlist = list(OrderedDict.fromkeys(wordlist))

for word in wordlist:
  print(duplicated.count(word),end= " ")