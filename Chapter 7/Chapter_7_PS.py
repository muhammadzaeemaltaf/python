# Q1. Write a program to print multiplication table of a given number using for loop.

# n = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# Q2. Write a program to greet all the person names stored in a list l1 and which starts with S.

l1 = ["Harry", "Sohan", "Sachin", "Rahul", "Sourav", "Sameer"]

# for name in l1:
#     if(name.startswith("S")):
#         print("Hello " + name)

# Q3. Attempt problem 2 using a while loop.

# i = 0

# while i < len(l1):
#     if(l1[i].startswith("S")):
#         print("Hello " + l1[i])
#     i += 1


# Q4. Write a program to find whether a given number is prime or not.

# n = int(input("Enter a number: "))

# for i in range(2, n):
#     if n % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")

# Q5. Write a program to find the sum of first n natural numbers using a while loop.

# n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print(sum)


# Q6. Write a program to print the factorial of a given number.

# n = int(input("Enter a number: "))

# fact = 1

# for i in range(1, n + 1):
#     fact *= i
# print(fact)


# Q7. Write a program to print the following pattern.
'''
  *  
 *** 
*****   n=3
'''    


# n = int(input("Enter a number: ")) 

# for i in range(1, n + 1):
#     print(" " * (n-i), end="")
#     print("*"*(2*i -1), end="")
#     print('')


# Q8. Write a program to print the following pattern.
'''
*  
** 
***   n=3
'''

# n = int(input("Enter a number: ")) 

# for i in range(1, n + 1):
#     print("*" * i)


# Q9. Write a program to print the following pattern.
'''
***
* *
***  n=3
'''


# n = int(input("Enter a number: ")) 

# for i in range(1, n + 1):
#   if i == 1 or i == n:
#     print("*"*n, end="")
#   else:
#     print("*", end="")
#     print(" "*(n-2), end="")
#     print("*", end="")
#   print("")


# Q10. Write a program to print multiplication table of a given number using for loop in reverse order.

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {11 - i} = {n*( 11 - i)}")
    