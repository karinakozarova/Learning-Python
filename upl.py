import os
from subprocess import call
import sys

if __name__ == "__main__":
    print sys.argv[1]
    message = ""
    for i in range(1,len(sys.argv)):
        print sys.argv[i]
        message += sys.argv[i]
        message += " "

    result = 'git add . && git commit -m "' + message + '" && git push'
    print("Running: " + result)
    os.system(result) 
