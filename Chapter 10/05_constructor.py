class Employee:
    language = "Py"  
    salary = 50000   

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Constructor Called")

    def getInfo(self):  # dunder method which is called by default
        print(f"Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

zaeem = Employee("Zaeem", 150000, "TypeScript")

zaeem.getInfo()

