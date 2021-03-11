#Write a Python function that accepts a string and 
#calculate the number of upper case letters and lower case letters.
#Sample String:'The quick Brow Fox'
#Expected Output:
#No. of Upper case characters : 3
#No. of Lower case Characters : 12


def foxFox(str):
    upperl = 0
    lowerl = 0
    for char in str:
        if char.isupper():
            upperl +=1
        elif char.islower():
            lowerl +=1
    print("No. of Upper case characters : {} \nNo. of Lower case Characters :{}".format(upperl,lowerl))

foxFox('The quick Brow Fox')