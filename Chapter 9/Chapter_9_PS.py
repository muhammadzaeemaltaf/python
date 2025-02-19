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



