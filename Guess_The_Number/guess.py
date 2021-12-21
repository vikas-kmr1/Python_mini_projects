import random

def guess_number(x):

    random_number=random.randint(1,x)
    guess=0

    while (guess != random_number):
        guess=random.randint(1,x)

        if guess<random_number:
            print(f"Ahh, guess again ,{guess} is too low ")

        elif guess>random_number:
            print(f"Ahh, guess again , {guess} is too high")

    print(f"Yay,Congrats the computer have guessed the random number {guess} correctly:")  

guess_number(10)