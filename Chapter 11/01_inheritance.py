class Employee:
    company = "Google"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}")


# class Programmer:

#     company = "Microsoft"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The language is {self.language}")


class Programmer(Employee): 
    company = "Microsoft"
    def showLanguage(self, language):
        print(f"The language is {language}")

a = Employee()
b = Programmer()

print(a.company,
b.company)

b.showLanguage("Python")