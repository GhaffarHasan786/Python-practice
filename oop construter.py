class student:
    name = "ghaffar"
    age = 18
    language = "urdu"
    def __init__(self, name, language, age):
     self.name =name
     self.age = age
     self.language = language
     print("i am creating the first dunder")
     
    def getinfo(self):
        print(f"the name is {self.name}.the age is {self.age}")
    @staticmethod
    def getdisplay():
            print (f"the name is{student.name}. the language is{student.language}")












room = student("ghaffar", "urdu", 18)

print(room.name, room.age)
#room.name = "ali" # object or instance attribute
#room.getinfo()
#room.getdisplay()