# Q1. write a program to store seven fruits in a list entered by the user.

# long code
fruits = []

# f1 = input("Enter fruit 1: ")
# fruits.append(f1)
# f2 = input("Enter fruit 2: ")
# fruits.append(f2)
# f3 = input("Enter fruit 3: ")
# fruits.append(f3)
# f4 = input("Enter fruit 4: ")
# fruits.append(f4)
# f5 = input("Enter fruit 5: ")
# fruits.append(f5)
# f6 = input("Enter fruit 6: ")
# fruits.append(f6)
# f7 = input("Enter fruit 7: ")
# fruits.append(f7)
# # print(fruits)

# Chort code
# fruits = [input(f"Enter fruit {i+1}: ") for i in range(7)]
# print(fruits)


# Q2. Write a program to accept marks of 6 students and display them in a sorted manner.

# marks = [int(input("Enter narks here: ")) for i  in range(6)]
# marks.sort()
# print(marks)

# Q3. Check that a tuple type cannot be changed in python.

t = (1, 2, 3, 4)

# t[0] = 34
# print(t)

# Q4. Write a program to sum a list with 4 numbers.

l= [2,54,54,43]
# print(sum(l))per

# Q5. Write a program to count the number of zeros in the following tuple.

t = (7, 8, 0, 7, 0, 9, 0)

n = t.count(0)

print(n)