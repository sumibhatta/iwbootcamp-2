#Write a Python function to multiply all the numbers in a list.
#Sample List : (8,2,3,-1,7)
#Expected Output : -336

def multi(list):
    prod= 1
    for item in list:
        prod *= item
    return prod


print(multi([8,2,3,-1,7]))
