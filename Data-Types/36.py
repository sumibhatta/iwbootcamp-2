#Write a Python program to sum all the items in a dictionary

dict = {1: 10, 2: 20, 3: 30, 4: 40, 7: 50, 6: 60}

val = 0
for value in dict.values():
    val = val + value

print(val)