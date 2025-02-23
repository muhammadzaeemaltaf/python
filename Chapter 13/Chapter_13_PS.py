# Q1. Write a program to input name, marks nad phone number of a student and format it using 
# the format() method.

# name = input("Enter your name: ")
# marks = input("Enter your marks: ")
# phone = input("Enter your phone number: ")

# print("Name: {}\nMarks: {}\nPhone: {}".format(name, marks, phone))

# Q2. A list contian the multiplication table of 9. Write a program to convert it to a vertical string of the same numbers.

# table = [str(9*i) for i in range(1, 11)]

# vs = "\n".join(table)
# print(vs)


# Q3. Write a program to filter a list of numbers which are divisible by 5.

# numbers = [12, 15, 60, 34, 55, 90, 100, 234, 345, 567, 789, 890, 1000]

# def find(x):
#     return x%5 == 0

# filtered = list(filter(find, numbers))
# print(filtered)


# Q4. Write a program to find the maximum of the numbers in a list using reduce function.

# from functools import reduce

# numbers = [12, 15, 60, 34, 55, 90, 1002, 100, 234, 345, 567, 789, 890, 1000]

# def greater(x, y):
#     return x if x > y else y

# print(reduce(greater, numbers))



# Q5. Explore 'Flask' module and create a web server using Flask & Pyhton
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "<p>Hello World! hahaha</p>"

app.run()