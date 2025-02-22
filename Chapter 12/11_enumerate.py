l = [1, 2, 3, 4, 5]

# index = 0
# for i in l:
#     print(f"The item number {index} is {i}")
#     index += 1  


# This can be simplified using enumerate

for index, item in enumerate(l):
    print(f"The item number {index} is {item}")
