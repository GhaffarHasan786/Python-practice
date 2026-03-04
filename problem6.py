name = input("enter your name: ")


print(f"afternoon, {name}")


#problem7
letter = ''' dear <|name|>,
         you are selected!
         <|date|>'''


print(letter.replace("<|name|>","harry").replace("<|date|>","8 october 2025"))