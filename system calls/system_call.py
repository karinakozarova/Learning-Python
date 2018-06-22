import os
from subprocess import call

if __name__ == "__main__":
    user_input = input("Which system function should I call? ")
    os.system(user_input) # first way
    print("")
    call(user_input) # second way