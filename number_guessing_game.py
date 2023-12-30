import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        guess = int(input("\nTake a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
            guessed = True

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_number()
    else:
        print("Thank you for playing!")

guess_number()
