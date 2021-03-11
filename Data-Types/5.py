#Write a Python program to add 'ing' at the end of a given string 
# (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'

string = "string"

if len(string) < 3:
    print(string)
elif string[-3:] == "ing":
    print(string + "ly")
else:
    print(string + "ing")
