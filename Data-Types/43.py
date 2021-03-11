#Write a Python program to remove an item from a tuple.

tup = (10, 20, 30, 40, 50, 60, 70)


lis = list(tup)
lis.pop()
tup = tuple(lis)
print(tup)