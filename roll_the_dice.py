import random

def random_upto(max = 6):
    return random.randint(1,max)

if __name__ == "__main__":
    print("Enter 'dice' to throw the dice or 'quit' to quit the app",end=" ")

    while True:
        user_command = input()

        if user_command == "quit":
            break
        elif user_command == "dice":
            print(random_upto())
        else:
            print("unknown command")