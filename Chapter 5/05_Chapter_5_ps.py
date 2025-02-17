# Q1. write a program to create a dictionary of Urdu words with their English meanings.
# Provide the user with an option to look it up.

words = {
    "madad": "help",
    "khushi": "happiness",
    "kamyaabi": "success",
}

# word = input("Enter a word to look up its meaning. ")
# print(words.get(word, "Word not found."))


# Q2. write a program to input eight numbers from the user and display all the unique numbers (once only).

# no = set([int(input("Enter a number: ")) for i in range(8)])
# print(no)

# Q3. can we have a set with 18 (int) and "18" (str) as its elements?

s = {18, "18"}
# print(s)


# Q4. What will be the length of the following set s?

s = set()
s.add(20)
s.add(20.0)
s.add("20")
# print(len(s))

# Q5. What will be the type of s?
s = {}
# print(type(s))

# Q6. Create a empty dictoinary. Allow 4 friends to enter their favorite language as values and
# use their names as keys.

# fav_lang = {}
# for i in range(4):
#     name = input("Enter your name: ")
#     lang = input("Enter your favorite language: ")
#     fav_lang[name] = lang

# print(fav_lang)

# Q7. Can you change the values inside a list which is contained in a set s?

s = {8, 7, 12, "hello"}
print(s)
