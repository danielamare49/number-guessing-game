import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7
won = False

while attempts < max_attempts:
    guess = int(input("Guess the number: "))

    attempts += 1

    if guess < secret:
        print("Too low!")

    elif guess > secret:
        print("Too high!")

    else:
        print(f"Correct! You got it in {attempts} attempts.")
        won = True
        break

if attempts == max_attempts and not won:
    print(f"Game over! {max_attempts} attempts used. The number was {secret}.")