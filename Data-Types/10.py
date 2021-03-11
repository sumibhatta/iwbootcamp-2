#Write a Python program to remove the characters which have odd index
#values of a given string.

string = "HeyYou"
newValue =""
for i in range(len(string)):
    if i%2 != 0:
        newValue = newValue+string[i]

print(newValue)