# Write a Python program to add an item in a tuple.

tup = (10, 20, 30, 40, 50, 60)
hi = 70

lis = list(tup)
lis.insert(6,hi)
tup = tuple(lis)
print(tup)