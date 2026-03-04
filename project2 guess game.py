import random
n = random.randint(1, 100)

g = -1
guesses = 1 
while(g != n):
    n = int(input("Guesses the number: "))
    guesses += 1
    if(g>n):
         print("lower number please: ")
         
    elif(g<n):
            print("higher number please: ")

print(f"you have guessed the {n} is correctly guesses {guesses} attempt")




