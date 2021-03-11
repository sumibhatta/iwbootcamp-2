#Write a Python function to sum all the numbers in a list.
#Sample List : (8,2,3,0,7)
#Expected Output: 20

def add_list(list):
    sum = 0
    for item in list:
        sum += item
    return sum


print(add_list([8, 2, 3, 0, 7]))
