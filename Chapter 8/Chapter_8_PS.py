# Q1. Write a program using function to find greatest of three numbers.

# def greatest_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print(greatest_of_three(a, b, c))


# Q2. Write a program using function to convert temperature from Celsius to Fahrenheit.

# def forenheit_to_celsius(fahrenheit):
#     return 5*(fahrenheit-32) / 9

# forenheit = float(input("Enter temperature in Celsius: "))
# print(f"{round(forenheit_to_celsius(forenheit))}C")


# Q3. How to prevent a python print() function to print a new line at the end?

# print("Hello")
# print("World", end=" ")
# print("Python", end=" ")


# Q4. Write a recursive function to calculate the sum of first n natural numbers.

# def sum_of_natural_numbers(n):
#     if n == 0:
#         return 0y

#     return n + sum_of_natural_numbers(n-1)

# n = int(input("Enter a number: "))
# print(sum_of_natural_numbers(n))


# Q5. Write a function to print fisrt n lines of the following pattern.
"""
***
**
*       for n = 3
"""


# def pattern(n):
#     if n == 0:
#         return
#     print("*" * (n))
#     pattern(n - 1)


# pattern(3)


# Q6. Write a function which convert inches to centimeters.

# def i_to_c(n):
#     return round(n/ 0.393701)

# n = float(input("Enter Inches: "))
# print(f"{n} inches in cm is:", i_to_c(n))


# Q7. write a python program to remove a given word from a string and strip it at the same time.

def rem(l, word):
    n = [item.replace(word, "").strip() for item in l]
    return n

l = ["johnal", "jacobali", "jingle", "heimer", "schmidt", "j"]
print(rem(l, "al"))
