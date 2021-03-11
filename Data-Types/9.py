#Write a Python program yo change the given string
# to a new string where the first and last chars have been exchanged.

def  firsLas(string):
    return string[-1:]+string[1:-1]+string[0:1]

pr = firsLas("Sumi")
print(pr)