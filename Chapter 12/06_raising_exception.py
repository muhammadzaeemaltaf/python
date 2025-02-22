# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a / b)

# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# except ValueError:
#     print("Please enter only numbers")
# except:
#     print("An error occurred")


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ZeroDivisionError("b cannot be 0.")

if type(a) != int or type(b) != int:
    raise ValueError("a and b must be integers.")

else:
    print(a / b)
