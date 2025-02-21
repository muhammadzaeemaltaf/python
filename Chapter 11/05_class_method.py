class Employee:
    a = 1
    @classmethod
    def show(cls):
        print("This class value of a is:",cls.a)

e = Employee()
e.a = 10
e.show()