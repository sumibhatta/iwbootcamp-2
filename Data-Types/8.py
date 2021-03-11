#Write a Python program to remove the nth index character
#from a nonempty string.


def removeNth(string, index):
    str1 = string[:index]
    str2 = string[index+1:]
    return (str1+str2)

r = removeNth("Hello", 1)
print(r)