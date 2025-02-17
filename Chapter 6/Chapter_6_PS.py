# Q1. Write a program to find greatest of four numbers entered by the user.

# a1 = int(input("Enter first number: "))
# a2 = int(input("Enter second number: "))
# a3 = int(input("Enter third number: "))
# a4 = int(input("Enter fourth number: "))

# if a1 > a2 and a1 > a3 and a1 > a4:
#     print("a1 number is the greatest: ", a1)
# elif a2 > a1 and a2 > a3 and a2 > a4:
#     print("a2 number is the greatest: ", a2)
# elif a3 > a1 and a3 > a2 and a3 > a4:
#     print("a3 number is the greatest: ", a3)
# else:
#     print("a4 number is the greatest: ", a4)

# Q2. Write a program to find out whether a student is pass or fail, if it requires a total of 40%
# and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# sub1 = int(input("Enter marks of first subject: "))
# sub2 = int(input("Enter marks of second subject: "))
# sub3 = int(input("Enter marks of third subject: "))

# total = sub1 + sub2 + sub3
# percentage = (total / 300) * 100

# if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and percentage >= 40:
#     print("Student is pass. ", percentage, "%")
# else:
#     print("Student is fail")


# Q3. A spam comment is defined as a text containing the following keywords: "make a lot of money", "buy now",
# "subscribe this", "click this". Write a program to detect these spams.

# comment = input("Enter your comment: ").lower()

# spams = ["make a lot of money", "buy now","subscribe this", "click this"]

# if any(spam in comment for spam in spams):
#     print("Spam detected")
# else:
#     print("No spam detected")


# Q4. Write a program to find whether a given username contains less than 10 characters or not.

# username = input("Enter your username: ")

# if len(username) < 10:
#     print("Username contains less than 10 characters")
# else:
#     print("Username contains more than 10 characters")

# Q5. Write a program which finds out whether a given name is present in a list or not.

# names = ["John", "Doe", "Jane", "Smith", "Alice", "Bob"]

# name = input("Enter your name: ").title()

# if name in names:
#     print("Name is present in the list")
# else:
#     print("Name is not present in the list")

# Q6. Write a program which finds out grade of a student from his marks from the following scheme:
# 90 - 100: Excellent
# 80 - 90: A
# 70 - 80: B
# 60 - 70: C
# 50 - 60: D
# < 50: Fail

# marks = int(input("Enter your marks: "))

# if marks >= 90 and marks <= 100:
#     print("Excellent")
# elif marks >= 80 and marks < 90:
#     print("A")
# elif marks >= 70 and marks < 80:
#     print("B")
# elif marks >= 60 and marks < 70:
#     print("C")
# elif marks >= 50 and marks < 60:
#     print("D")
# else:
#     print("Fail")


# Q7. Write a program to find out whether a given post is talking about "Harry" or not.

post = input("Enter your post: ").lower()

if "harry" in post:
    print("Post is talking about Harry")
else:
    print("Post is not talking about Harry")