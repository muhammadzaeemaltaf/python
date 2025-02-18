import random

"""
1 for snake
-1 for water
0 for gun
"""

computer = random.choice([-1, 0, 1])
player = input("Enter Your Choice: ").upper()
playerDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
playerNum = playerDict[player]

print(f"Computer's Choice: {reverseDict[computer]} \nYour Choice: {reverseDict[playerNum]} \n")

if computer == playerNum:
    print("Draw")
else:
    if computer == -1 and playerNum == 1:
        print("You Win")
    elif computer == -1 and playerNum == 0:
        print("You Lose")
    elif computer == 1 and playerNum == -1:
        print("You Lose")
    elif computer == 1 and playerNum == 0:
        print("You Win")
    elif computer == 0 and playerNum == -1:
        print("You Win")
    elif computer == 0 and playerNum == 1:
        print("You Lose")
    else:
        print("Something Went Wrong")
