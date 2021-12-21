import random

randomNum = random.randint(1,10)
i = 0
while True:
    guess = int(input("Choose a number 1-10: "))
    if guess<randomNum:
        print("Too low, try again! ")
    elif guess > randomNum:
        print("Too high, try again! ")
    else:
        print("Good job! You guessed that the mystery number was {}. ".format(randomNum))
        again = input("Do you want to play again? (y/n)")
        if again == "y":
            randomNum = random.randint(1,10)
            guess = 0
        else:
            print("Thanks for playing!")
            break