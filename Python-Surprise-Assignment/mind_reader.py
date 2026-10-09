
import random
import time

print("=" * 40)
print("       MIND READER GAME")
print("=" * 40)

name = input("What is your name? ")

play_again = "yes"

while play_again == "yes":

    secret_number = random.randint(1, 100)
    attempts = 7
    won = False

    start_time = time.time()

    print("\nHello", name + "!")
    print("I am thinking of a number between 1 and 100.")
    print("You have 7 chances to guess it.")

    while attempts > 0:

        print("\nChances left:", attempts)
        guess = int(input("Enter your guess: "))

        attempts = attempts - 1

        if guess == secret_number:
            print("AMAZING! You read my mind!")
            won = True
            break

        elif guess < secret_number:
            print("Too low! Try a bigger number.")

        else:
            print("Too high! Try a smaller number.")

    end_time = time.time()
    elapsed_time = int(end_time - start_time)

    if won == True:
        print("\nCongratulations,", name + "!")
        print("The secret number was", secret_number)
        print("You finished in", elapsed_time, "seconds.")
        print("Your score:", attempts * 10 + max(0, 30 - elapsed_time))

    else:
        print("\nGAME OVER!")
        print("The secret number was", secret_number)

    play_again = input("Play again? (yes/no): ")

print("\nThanks for playing,", name + "!")
