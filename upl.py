import os
from subprocess import call
import sys

if __name__ == "__main__":
    print sys.argv[1]
    message = ""
    for i in range(1,len(sys.argv)):
        print sys.argv[i]
        message += sys.argv[i]
    print message
    os.system('git add . && git commit -m "added more python exercises" && git push') 
