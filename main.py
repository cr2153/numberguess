import random


def main():
    random_number = random.randint(1, 100)
    attempts = 0
    while(True):
        userinput = input("Please enter guess: ")
        try:
            userinput = int(userinput)
        except ValueError:
            print("error: please enter an integer")
            continue
        if userinput != random_number:
            attempts += 1
            if userinput < random_number:
                print('Too low, try again')
            else:
                print('Too high, try again')
        else:
            print(f'Congrats! you got it, the number was {random_number} and you took {attempts+1} attempt(s) to get it.')
            break
if __name__ == "__main__":
    main()
    while (input("Play again?[y/n] ").lower() == "y"):
        main()