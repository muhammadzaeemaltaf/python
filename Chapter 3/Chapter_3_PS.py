# Q1. Write a python program to display a user entered name followed by Good Afternoon using input() function.

# name = input("Enter your name: ")
# print(f"Good Afternoon {name.title()}")

# Q2. Write a python program to fill in a letter template given below with name and date.
# letter = 'Dear <|Name|>, You are selected! Date: <|Date|>'


letter = """Dear <|Name|>, 
You are selected!
Date: <|Date|>"""
# print(letter.replace('<|Name|>', "Zaeem").replace('<|Date|>', "12-2-2025"))

# Q3. Write a python program to detect double spaces in a string.

name = "Zaeem is  learning  python"
# print(name.find("  "))

# Q4. Replace double spaces with single spaces
name = "Zaeem is  learning  python"
# print(name.replace("  ", " "))

# Q5. Write a python program to format the following letter using escape sequence characters.
letter = "Dear Zaeem,\n\tThis Python course is nice!\nThanks!"
print(letter)