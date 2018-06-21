import random

def get_random_int():
    return random.randint(1,101)

if __name__ == "__main__":
    num_to_guess = get_random_int()
    print(num_to_guess)
    while True:
        user_input = int(input("Reading input: "))
        if(user_input == num_to_guess):
            print("Output: YAY")
            break
        elif user_input > num_to_guess:
            print("Output: LOWWWWER")
        else:
            print("Output: HIGHERRR")
    print("Output: GAME OVER")