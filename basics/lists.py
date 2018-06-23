from sys import stdin
import re
"""
The first line contains an integer,N , denoting the number of commands.
Each line of the subsequent lines contains one of the commands:
    insert i e: Insert integer at position .
    print: Print the list.
    remove e: Delete the first occurrence of integer .
    append e: Insert integer at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.
"""

def input_to_list(userinput):
    return re.sub("[^\w]", " ",  userinput).split()

if __name__ == '__main__':
    N = int(input())
    list = []

    for i in range(0,N):
        userinput = stdin.readline()
        wordList = input_to_list(userinput)

        if "insert" == wordList[0]:
            list.insert(int(wordList[1]),int(wordList[2]))
        elif "print" in userinput:
            print(list)
        elif "remove" in userinput:
            list.remove(int(wordList[1]))
        elif "append" in userinput:
            list.append(int(wordList[1]))
        elif "sort" in userinput:
            list.sort()
        elif "pop" in userinput:
            list.pop()
        elif "reverse" in userinput:
            list.reverse()