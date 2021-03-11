#Write a Python program to add all the items in a list.


def add_list(list):
    sum = 0
    for item in list:
        sum += item
    return sum

li =[1,2,3,4,5,6]
print(add_list(li))
