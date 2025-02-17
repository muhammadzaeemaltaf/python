# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()


import os

directory_path = "/"

content = os.listdir(directory_path)

for item in content:
    print(item)
    # print(os.path.join(directory_path, item))
    # print(os.path.abspath(item))
    # print(os.path.abspath(directory_path))