#Data Types1
#Write a Python program to count the number of characters
#(characterfrequency) in a string. Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

string = "google.com"

dict = {}

for char in string:
    dict[char] = dict.get(char, 0) +1
    #Returns the value of key,and set value to 0 for new character
    # return by increament otherwise 

print(dict)
    