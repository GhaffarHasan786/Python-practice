word = "donkey"

with open("donkey file.txt", "r" ) as f:
    content = f.read()

    contentnew = content.replace(word, "#####")

    with open("donkey file.txt", "w") as f:
        f.write(contentnew)
        print(contentnew)