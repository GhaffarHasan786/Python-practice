class employee:
    company = "arfa ict"
    name = "defualt name"
    def show(self):
        print(f"the employee name is {self.name},and the company is {self.company}")

class coder:
       language ="python"
       def printlanguage(self):
        print(f"the all language is {self.language}")

class programmer(employee,coder):
    company = "arfa karim"
    def showlanguage(self):
         print(f"the employee company is {self.company},and the language is {self.language}")






a=employee()
b =programmer()
#print(a.language,b.name,c.language)
b.printlanguage()
b.show()
b.showlanguage()