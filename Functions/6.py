#Write a Python function to check whether a number is in a given range.

def numnum(num, srange, erange):
    if num in range(srange,erange):
        print("In range")
    else:
        print("Not in range")

numnum(1,1,7)
numnum(7,1,7) #Careful takes 1st emement but excludes last 
numnum(4,1,7)


