import random

from PIL import Image
end=100
def show_board():
     img=Image.open('./Python_mini_projects/snake_and_Ladder/snake_ladder.png')
     print(img)
     img.show()
show_board()

def check_ladder(points):
     if points==4:
          print("Ladder")
          return 25
     elif points==13:
          print("Ladder")
          return 46
     elif points==33:
          print("Ladder")
          return 49
     elif points==50:
          print("Ladder")
          return 69
     elif points==42:
          print("Ladder")
          return 63
     elif points==62:
          print("Ladder")
          return 81
     elif points==74:
          print("Ladder")
          return 92
     else:
          return points

def check_snake(points):
     if points==40:
          print("Snake:")
          return 3
     elif points==27:
          print("Snake:")
          return 5
     elif points==43:
          print("Snake:")
          return 18
     elif points==54:
          print("Snake:")
          return 31
     elif points==89:
          print("Snake:")
          return 53
     elif points==66:
          print("Snake:")
          return 45
     elif points==76:
          print("Snake:")
          return 58
     elif points==99:
          print("Snake:")
          return 41
     else:
          return points

def reached_end(points):
     if points==end:
          return True
     else:
          return False



def play():
     p1_name=input("Player-1 Name:")
     p2_name=input("Player-2 Name:")
     p1_score = 0
     p2_score = 0
     turn=0
     while(True):
          if turn%2==0:
               print("--------------------\n---->",p1_name," Turn\n------------------\n")

               c=int(input("\nPress 1 to continue, 0 to Quit:"))
               if c==0:
                    print(p1_name,"scored: ",p1_score)
                    print(p2_name,"scored: ",p2_score)
                    print("Qutting the game ,Thanks for Playing ")
                    break
               dice=random.randint(1,6)
               print("dice showed: ",dice,end="\n")

               p1_score+=dice;
               p1_score=check_ladder(p1_score)
               p1_score=check_snake(p1_score)

               if(p1_score>end):
                    p1_score=end

               print(p1_name,"Your Score: ",p1_score)

               if reached_end(p1_score):
                    print(p1_name,"Won")
                    break



          if(turn%2==1):
               print("-------------------\n---->",p2_name," Turn\n------------------")

               c = int(input("\nPress 1 to continue, 0 to Quit:"))
               if c == 0:
                    print(p1_name, "scored: ", p1_score)
                    print(p2_name, "scored: ", p2_score)
                    print("Qutting the game ,Thanks for Playing ")
                    break
               dice = random.randint(1, 6)
               print("dice showed: ", dice,end="\n")

               p2_score += dice;
               p2_score = check_ladder(p2_score)
               p2_score = check_snake(p2_score)

               if (p2_score > end):
                    p2_score = end
               print(p2_name, "Your Score: ", p2_score)

               if reached_end(p2_score):
                    print(p2_name, "Won")
                    break

          turn += 1

play()