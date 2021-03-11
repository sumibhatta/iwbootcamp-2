#Write a Python program to reverse a string.
#Sample String:"1234abcd"
#Expected Output:"dcba4321"

def reverString(string):
    return string[-1:0:-1]


print(reverString('1234abcd'))