"""
create a simple number guessing game.
The user gets 10 chances to guess a number.
If the user guesses the number before 10 chances, stop asking the number from the user , say congrats and end the game
If the user never guesses the number , ask them 10 times and then end the game!!
"""
import random

num = 1

print("Welcome to the number guessing game!! We have a number to be guessed. You have 10 chances.")
print("Your secret number is b/w 1 and 50")
secret_number = random.randint(1, 50)
attempts = 10
is_guess_correct = False

while num <= 10:
    print(f"You have {attempts} chances to guess the number")
    user_number = int(input("Enter your guess: "))
    if user_number == secret_number:
        print("Congratulations! You guessed the number!")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"Your guess is wrong! Try {higher_or_lower} number.")
    num += 1
    attempts -= 1

if not is_guess_correct:
    print("BAD LUCK! You exhausted all your attempts and couldn't guess the number")
print(f"The secret number was {secret_number} . GAME OVER!!")
