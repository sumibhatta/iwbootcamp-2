#Write a Python program to print the even numbers from a given list.
#Sample List :[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result:[2, 4, 6, 8]

def EvenNumber(list):
    li = []
    for item in list:
        if(item%2 == 0):
            li.append(item)
    print(li)


EvenNumber([1, 2, 3, 4, 5, 6, 7, 8, 9])