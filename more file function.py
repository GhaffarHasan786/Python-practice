#f = open("file.txt")

#lines = f.readlines()
#print(lines ,type(lines))

#line function
''''''
f =open("file.txt")

line1 =f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 =f.readline()
print(line3)
line4 =f.readline()
print(line4)

f.close()
''''''
f =open("file.txt")
line =f.readlines()
while(line !=" "):
    print(line)
lines = f.readline()
f.close()
