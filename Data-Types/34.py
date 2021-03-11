#Write a Python script to merge two Python dictionaries.
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 7: 50, 6: 60}
dict2 = {1: 1, 8: 4, 9: 9, 10: 16, 11: 25}

dict1.update(dict2)
print(dict1)