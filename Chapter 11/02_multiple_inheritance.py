class Employee:
    company = "Google"
    name = "Sachin"

    def show(self):
        print(f"The name of Employee is {self.name} and the company is {self.company}")


class Coder:
    language = "Python"

    def printLanguage(self):
        print(f"Out of all the language is {self.language}")


class Programmer(Employee, Coder):
    company = "Microsoft"

    def showLanguage(self):
        print(f"The language is {self.language}")


a = Employee()
b = Programmer()

# print(a.company, b.company)
b.show()
b.showLanguage()
b.printLanguage()
