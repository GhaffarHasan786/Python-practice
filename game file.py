import random


def game():
    print("You are playing the game... ")
    score = random.randint(1, 100)
    #fetch the score
    with open("hiscore.txt") as f:
     hiscore = f.read()
     if(hiscore!=""):
        hiscore = int(hiscore)
     else:
        hiscore = 0
        print(f"your score: {score}")
        if(score>hiscore):
        # write the score and write file
         with open("hiscore.txt" , "w") as f:
           f.write(str(score)) 
           return score
         print(score)
game()