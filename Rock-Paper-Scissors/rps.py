import random

def user_Wins(computer,user):
    #s>p , p>r, r>s

    if (user.lower()=='s' and computer.lower()=='p') or (user.lower()=='p' and computer.lower()=='r') or (user.lower()=='r' and computer.lower()=='s'):
        return True
    return False   

def play():
    user=input("\nRock(r/R),\n Paper(P/p)\n Scissor(S/s):\n ==> ")
    computer=random.choice(['r','w','s'])

    if user==computer:
        return "Tie"

    if (user_Wins(computer,user)):
        return "You Win 😁"
    return "You Lost 😒"    

mwnu=""
while(True):
    menu=input("\nC-Continue \n E-Exit ==>") 
    if menu.lower()=='e':
        break  
    print(play())
