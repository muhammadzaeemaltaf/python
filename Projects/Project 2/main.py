from random import randint

guesses = 0
while True:
    try:
        guesses += 1
        userGuess = int(input("Enter your guess between 1 - 10: "))
        if userGuess < 1 or userGuess > 10:
            print("\n===== Please enter a number between 1 and 10 =====\n")
            continue

        randomNumber = randint(1, 10)

        if userGuess == randomNumber:
            print(f"Hurray!! You guessed correctly in {guesses} guesses")
            break
        elif userGuess < randomNumber:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

    except ValueError:
        print("\n===== Invalid input! Please enter a number between 1 and 10 =====\n")
