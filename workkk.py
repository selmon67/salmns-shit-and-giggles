import random

low = 100
high = 1000
program = random.randint(low, high)
attempt = 0

status = True
while status:
    guess = (input(f"guess a number between {low} and {high}: "))
    if guess.isdigit():
        guess = int(guess)
        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
        elif guess > program:
            print(f"Please enter a number between {low} and {high}.")
        elif guess < program:
            print("Too low! Try again.")
        elif guess > program:
            print("Too high! Try again.")
            attempt += 1
        else:
            print("Congratulations! You've guessed the correct number!")
            print(f"It took you {attempt} attempts.")
            status = False
    else:
        print("Please enter a valid number.")

    