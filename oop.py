class student:
    name = "ghaffar"
    age = 18
    language = "urdu"
   # def getinfo(self):
        #print(f"the name is {self.name}.the age is {self.age}")
    @staticmethod
    def getdisplay():
            print (f"the name is{student.name}. the language is{student.language}")












room = student()
#room.name = "ali" # object or instance attribute
#room.getinfo()
room.getdisplay()