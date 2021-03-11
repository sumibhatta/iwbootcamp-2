#Write a Python script to check whether a given key already exists
#in a dictionary.

def checkDuplicate(dict, key):
    if key in dict:
         print("Oh! the there is duplicate key")
    else:
        print("No duplicate :) ")

# def checkDuplicate(dict, key):
#     li =[]
#     li = dict.keys()
#     li.append(key)
#     if(len(li) != len(set(li))):
#         print("Oh! the there is duplicate key")
#     else:
#         print("No duplicate :) ")

checkDuplicate({1: 10, 2: 20, 3: 30, 4: 40, 7: 50, 6: 60},5)