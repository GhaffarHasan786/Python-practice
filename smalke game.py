import random


computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"S": 1 ,"W": -1 ,"G": 0}
reversedict = {1:"snake", -1:"water", 0:"gun"}
you = youdict[youstr]

print(f"your choice{reversedict[you]}\n computer choice{reversedict[computer]}")

if(computer==you):
    print("its a draw")
else:
    ''''''
    if(computer ==-1 and you ==1):
        print("you wins!")
    elif(computer ==-1 and you ==0):
        print("you lose!")
    elif(computer ==1 and you ==0):
        print("you wins!")
    elif(computer ==1 and you ==-1):
        print("you lose!")
    elif(computer ==0 and you ==-1):
        print("you wins!")
    elif(computer ==0 and you ==1):
        print("you lose!")
    else:
        print("something went wrong: ")
        ''''''

    
        if((computer - you)==-1 or (computer - you)==2):
            print("you lose!")
        else:
            print("you wins!")
            