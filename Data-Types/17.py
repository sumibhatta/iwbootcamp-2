#Write a Python program to multiplies all the items in a list.

def mul_list(list):
    prod = 1
    for item in list:
        prod *= item
    return prod

li =[1,2,3,4,5,6]
print(mul_list(li))
