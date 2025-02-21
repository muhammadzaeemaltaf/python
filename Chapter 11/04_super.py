class Employee:

    def __init__(self):
        print("Employee created")
    a = 1


class Programmer(Employee):
    
    def __init__(self):
        print("Programmer created")
    b = 2


class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Manager created")
    c = 3


m = Manager()
print(m.a, m.b, m.c)
