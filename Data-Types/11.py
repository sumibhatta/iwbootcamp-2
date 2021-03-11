#Write a Python program to count the occurrences of each word in a given
#sentence.

string = "Hello Hello Progammers, how are you?"

list = string.split()
dict = {}
for word in list:
    dict[word] = dict.get(word, 0) +1

print(dict)