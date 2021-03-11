#Write a Python program to insert a given string at the beginning 
#of all items in a list.
#Sample list : [1,2,3,4], string : emp
#Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

def addString(lis, str):
    newList = []
    for item in lis:
        newList.append(str+"{}".format(item))
    return newList

print(addString([1,2,3,4], 'emp'))
