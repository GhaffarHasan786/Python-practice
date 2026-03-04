class employee:
    company = "arfa ict"
    def show(self):
        print(f"the employee name is {self.name},and the language is {self.language}")


# class programmer:
#     company = "arfa karim"
#     def show(self):
#         print(f"the employee is {self.name},and the salary is {self.salary}")
#     def showlanguage(self):
#         print(f"the employee name is {self.name},and the salary is {self.salary}")

class programmer(employee):
    company = "arfa karim"
def showlanguage(self):
    print(f"the employee name is {self.name},and the language is {self.language}")






a=employee()
b =programmer()
print(a.company, b.company)
