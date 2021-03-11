#Write a Python program to check whether all dictionaries in a list 
# are empty or not.
#Sample list : [{},{},{}]
#Return value : True
#Sample list : [{1,2},{},{}]
#Return value : False

li =[{1,2},{},{}]
a = True
for i in li:
     a = a + any(i)

if(a == 1):
    print("True")
else:
    print("False")