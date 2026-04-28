import random


def main():
    random_number = 0
    while True:
        difficulty = input("Please enter a difficulty option. [E/M/H] ").lower()
        if difficulty == 'e':
            random_number = random.randint(1, 50)
            break
        elif difficulty == 'm':
            random_number = random.randint(1, 100)
            break
        elif difficulty == 'h':
            random_number = random.randint(1, 200)
            break
        else:
            print('Please enter a valid character. "e" for easy, Etc.')


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