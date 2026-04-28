import random

def main():
    random_number = 0
    dictionary = {'e':50, 'm':100, 'h':200}
    while True:
        selection = input("Please choose a difficulty [E/M/H]: ").lower()
        if selection in dictionary:
            random_number = random.randint(1, dictionary[selection])
            break
        else:
            print("Please enter a valid difficulty, for example, 'e' for easy.")

    attempts = 0
    while True:
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