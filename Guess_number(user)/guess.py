import random
def computer_guess(num):
    low = 1
    high = num
    hint =""

    while hint!='c':
        if(low!=high):
            guess=random.randint(low,high)
        else:    
            guess=low
        hint=input(f'''Is {guess},
        too high(h),
        too low(l),
        correct (c): 
        =>''')
        if(hint.lower() =='h' ):
            high=guess-1

        if (hint.lower()=='l'):
            low=guess+1
    print(f"Yay, the computer guessed your number {num} corrrectly:")


computer_guess(100)