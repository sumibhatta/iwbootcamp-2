#Write a Python function to find the Max of three numbers

def maxOfThree(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

max = maxOfThree(6,4,1)
print("{} is the greatest number".format(max))