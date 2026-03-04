# try:
#  a = int(input("Hey, Enter the number: "))
 
#  print(a)
# except Exception as e:


#  print(e)



# raising exception
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if(b == 0):
     raise ZeroDivisionError("hey,you program means the not execute")
else:
 print(f"the division a/b is {a/b}")