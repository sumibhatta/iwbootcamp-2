#Write a Python program to check a list is empty or not.

def checkIfEmpty(li):
    if not li:
        print("Empty")
    else:
        print("Not Empty")


lisOne = []
checkIfEmpty(lisOne)
lisTwo = [2, 5, 1, 2, 4, 4, 2, 3, 2, 1]
checkIfEmpty(lisTwo)