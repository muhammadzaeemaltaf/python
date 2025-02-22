try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print("An exception occurred: ", e)

else:
    print("No exception occurred")