
try:
    a = int(input("Enter a number: "))
    print(a)

# except ValueError:
#     print("Invalid input")
except Exception as e:
    print("Invalid input")
    print(e)