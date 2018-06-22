
if __name__ == "__main__":
    while True:
        try:
            x = int(input("Enter a number: "))
            break
        except ValueError:
            print("Can't parse! Try again ")
    print("The number is " + str(x))