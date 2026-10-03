# 21_guessing_game.py

secret_number = 50

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print("Correct! You found the number.")
        break