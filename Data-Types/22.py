#Write a Python program to remove duplicates from a list.

lis = [2, 5, 1, 2, 4, 4, 2, 3, 2, 1]

toSet = set(lis)
toList = list(toSet)
print(toList)