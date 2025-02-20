class Employee:
    language = "Py"  
    salary = 50000   

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

zaeem = Employee()
# zaeem.language = "JavaScript"
zaeem.greet()