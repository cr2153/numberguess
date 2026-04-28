import random

def main():
    random_number = 0
    dictionary = {'e':50, 'm':100, 'h':200} # contains max random value for each difficulty
    while True:
        selection = input("Please choose a difficulty [E/M/H]: ").lower()
        if selection in dictionary:
            random_number = random.randint(1, dictionary[selection]) # generates a random int from 1 to the dictionary value of the difficulty level.
            break
        else:
            print("Please enter a valid difficulty, for example, 'e' for easy.")

    attempts = 0
    while True:
        userinput = input("Please enter guess: ")
        try:
            userinput = int(userinput) # try block to perform input validation
        except ValueError:
            print("error: please enter an integer")
            continue
        if userinput != random_number:
            attempts += 1 #increase attempts counter by one if incorrect
            if userinput < random_number:
                print('Too low, try again')
            else:
                print('Too high, try again')
        else:
            print(f'Congrats! you got it, the number was {random_number} and you took {attempts+1} attempt(s) to get it.') # uses fstring to print results of game
            break
if __name__ == "__main__":
    main()
    while (input("Play again?[y/n] ").lower() == "y"): # asks the user if they want to play again.
        main()
