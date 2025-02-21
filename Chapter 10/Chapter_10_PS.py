# Q1. Create a class "Programmer" for storing information of a programmer working in Microsoft.

# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p = Programmer("John", 10000, 1234)
# print(p.name, p.salary, p.pin, p.company)

# r = Programmer("roman", 120000, 134)
# print(r.name, r.salary, r.pin, r.company)


# Q2. Create a class "Calculator" capable of finding square, cube and squareroot of a number.

# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square of {self.n} is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube of {self.n} is {self.n**3}")

#     def sqroot(self):
#         print(f"The square root of {self.n} is {round(self.n**0.5)}")


# a = Calculator(4)
# a.square()
# a.cube()
# a.sqroot()


# Q3. Create a class with a class attribute 'a'; create an object from it and set 'a' directly.
# The goal is to see if setting the attribute on an object changes the class attribute.

# class A:
#     a = 1  # Class attribute 'a' is set to 1

# obj = A()  # Create an instance of class A
# obj.a = 0  # Set the attribute 'a' on the instance to 0.
#          # This creates an instance attribute 'a', which shadows the class attribute.

# # print(obj.a)  # Prints the instance's 'a' value, which is 0


# Q4. Add static method in problem 2, to greet the user with "Hello"

# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square of {self.n} is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube of {self.n} is {self.n**3}")

#     def sqroot(self):
#         print(f"The square root of {self.n} is {round(self.n**0.5)}")

#     @staticmethod
#     def greet():
#         print("Hello")


# a = Calculator(4)
# a.greet()
# a.square()
# a.cube()
# a.sqroot()


# Q5. Write a class Train which has methods to book a ticket, get status(no of seats)
# and get fare information of trains running under Indian Railways.
# from random import randint


# class Train:
#     def __init__(self, trainNo):
#         self.trainNo = trainNo

#     def book(self, frm, to):
#         print(f"Ticket Booked in train no: {self.trainNo} from {frm} to {to}")

#     def getStatus(self,):
#         print(f"Train no: {self.trainNo} has {randint(0, 100)} seats available")

#     def getFare(self, frm, to):
#         print(
#             f"Ticket fare in train no: {self.trainNo} from {frm} to {to} is {randint(200, 1000)}"
#         )


# t = Train(12345)
# t.book("Delhi", "Mumbai")
# t.getStatus()
# t.getFare("Delhi", "Mumbai")




# Q6. Can you change a self-parameter inside a class to something else (say 'zaeem')?
# Try changing self to 'slf' or 'zaeem' and see if it works.

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(zaeem, frm, to):
        print(f"Ticket Booked in train no: {zaeem.trainNo} from {frm} to {to}")

    def getStatus(self,):
        print(f"Train no: {self.trainNo} has 10 seats available")

    def getFare(self, frm, to):
        print(
            f"Ticket fare in train no: {self.trainNo} from {frm} to {to} is 20009"
        )


t = Train(12345)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")