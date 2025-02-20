class Employee:
    language = "Py"  # class attribute
    salary = 50000   # class attribute

zaeem = Employee()
zaeem.language = "JavaScript"
print(zaeem.language, zaeem.salary)