import os
import sys

def get_commit_message():
    commit_message = ""
    for i in range(1,len(sys.argv)):
        commit_message += sys.argv[i]
        commit_message += " "
    return commit_message

if __name__ == "__main__":
    query = 'git add . && git commit -m "' + get_commit_message() + '" && git push'
    print("Running: " + query)
    os.system(query) 
