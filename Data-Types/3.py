#Write a Python program to get a string from a given string where all
#occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'

string = "restart"

temp = string[0]
str = string.replace (temp, '$')
str = temp + str[1:]
print(str)
