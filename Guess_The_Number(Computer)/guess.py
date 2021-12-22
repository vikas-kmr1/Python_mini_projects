import random

def guess_number():
    high= random.randrange(1,199,4)
    low=1
    random_number=random.randint(low,high)
    guess=0


    while (guess != random_number):
        guess=int(input(f"Guess a number b/w {low} and {high}:  "))

        if guess<random_number:
            print(f"Ahh, guess again ,{guess} is too low ")
            low=guess

        elif guess>random_number:
            print(f"Ahh, guess again , {guess} is too high")
            high=guess

    print(f"Yay,Congrats the computer have guessed the number {guess} correctly:")  

guess_number()