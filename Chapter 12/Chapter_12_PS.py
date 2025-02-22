# Q1. Write a program to open file 1.txt, 2.txt, 3.txt  if any of the file is not present
# then it should print the message that file is not present.

# try:
#     with open("1.txt") as f:
#         print(f.read())

# except Exception as e:
#     print("File is not present")

# try:
#     with open("2.txt") as f:
#         print(f.read())

# except Exception as e:
#     print("File is not present")

# try:
#     with open("3.txt") as f:
#         print(f.read())

# except Exception as e:
#     print("File is not present")

# print("Thanks for using the program")


# Q2. Write a program to print third, fifth and seventh element from a list using enumerate function.

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for index, item in enumerate(list1):
#     if index == 2 or index == 4 or index == 6:
#         print(item)


# Q3. Write a list comprehension to print the multiplication table of a user input number.

# num = int(input("Enter the number: "))

# table = [ num*i for i in range(1,11)]
# print(table)


# Q4. Write a program to display a/b where a and b are integers. If b=0, 
# display infinite by handling the ZeroDivisionError.

# try:
#     a = int(input("Enter the number a: "))
#     b = int(input("Enter the number b: "))
#     print(a/b)

# except ZeroDivisionError as e: 
#     print("Infinite")


# Q5. Write a multiplication tables in problem 3 in a file Table.txt

num = int(input("Enter the number: "))

table = [ num*i for i in range(1,11)]

with open("Table.txt", "a") as f:
    f.write(f"Table of {num} is: {str(table)} \n")