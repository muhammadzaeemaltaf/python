def main():
    try:
        a = int(input("Enter a number: "))
        print(a)

    except Exception as e:
        print("An exception occurred: ", e)

    finally:
        print("Hey I am finally block, I will always execute whether exception occurs or not")

main()