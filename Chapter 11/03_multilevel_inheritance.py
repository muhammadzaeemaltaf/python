class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

m = Manager()
print(m.a, m.b, m.c)