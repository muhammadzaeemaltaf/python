class Employee:
    language = "Py"  # class attribute
    salary = 50000   # class attribute

zaeem = Employee()
zaeem.name = "Zaeem Altaf"   # instance attribute
print(zaeem.name , zaeem.language, zaeem.salary)
# Here name is belong to zaeem object as instance attribute and language and salary are class attributes