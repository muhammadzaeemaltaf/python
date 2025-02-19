# Q1. Write a program to read the text from a given file 'poem.txt' and find out whether it
# contain the word 'twinkle' or not.

# file = open("poem.txt")
# content = file.read()

# if 'twinkle' in content:
#     print("Yes, the word 'twinkle' is present in the file.")
# else:
#     print("No, the word 'twinkle' is not present in the file.")

# file.close()


# Q2. The game() function in a program lets the user play a game and returns the score as an integer.
# you need to read a file 'hiscore.txt' which is either blank or contains the previous high score.
# you need to write a program to update the file 'hiscore.txt' if the previous score was less than
# the current score.

# import random


# def game():
#     print("YOu are playing a game...")
#     score = random.randint(1, 60)
#     print("Your score is: ", score)

#     with open("hiscore.txt") as file:
#         hiscore = file.read()
#         if hiscore != "":
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     if score > (hiscore):
#         with open("hiscore.txt", "w") as file:
#             file.write(str(score))
#             print("Congratulations! You have broken the high score.")


#     return score

# game()


# Q3. Write a program to generate a multiplication table from 2 to 20 and write it in a different file.
# Please these files in folder for a 13 - years old.


# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} x {i} = {n*i} \n"

#     with open(f"tables/table_{n}.txt", "w") as file:
#         file.write(table)


# for i in range (2, 21):
#     generateTable(i)


# Q4. A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with
# "######" by updating the file.


# word = "Donkey"

# with open("file.txt") as file:
#     content = file.read()
#     if word in content:
#         with open("file.txt", "w") as file:
#             content = content.replace(word, "######")
#             file.write(content)


# Q5. Repeat a program 4 for a list of some words to be censored.

# words = ["Donkey", "Kaddu", "Mote"]

# for word in words:
#     with open("file.txt") as file:
#         content = file.read()
#         if word in content:
#             with open("file.txt", "w") as file:
#                 content = content.replace(word, "#" * len(word))
#                 file.write(content)


# Q6. Write a program to mine log file and find out whether it contains the word "python" or not.

# with open("log.txt") as file:
#     content = file.read()
#     if "Python" in content or  "python" in content:
#         print("Yes, the word 'Python' is present in the file.")
#     else:
#         print("No, the word 'Python' is not present in the file.") 


# Q7. Write a program to find out the line number where the word "Python" is present in the log file.

# with open("log.txt") as file:
#     content = file.readlines()
#     for i in range(len(content)):
#         if "Python" in content[i] or  "python" in content[i]:
#             print(f"The word 'Python' is present in the line number {i+1}.")
#             break
#     else:
#         print("The word 'Python' is not present in the file.")


# Q8. Write a program to make a copy of a file 'file.txt' and name it 'file_copy.txt'.

# with open("file.txt") as file:
#     content = file.read()

# with open("file_copy.txt", "w") as file:
#     file.write(content)


# Q9. Write a program to find out whether a file is identical & have same content as another file.

# with open("file.txt") as file:
#     content1 = file.read()

# with open("file_copy.txt") as file:
#     content2 = file.read()

# if content1 == content2:
#     print("The content of the files is identical.")
# else:
#     print("The content of the files is not identical.")


# Q10. Write a program to wipe out the content of a file 'file.txt'.

# with open("file_copy.txt", "w") as file:
#     file.write("")


# Q11. Write a program to rename a file to 'rename_by_python.txt'.

import os

with open("old.txt") as file:
    content = file.read()

with open("rename_by_python.txt", "w") as file:
    file.write(content)

os.remove("old.txt")
 