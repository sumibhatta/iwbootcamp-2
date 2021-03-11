#Write a Python program to find intersection of two given arrays using
#Lambda.
def interSection(arr1, arr2): 
     result = filter(lambda x: x in arr1, arr2)
     print("Intersection {}".format(result))

arr1 = [1, 2, 3, 4, 5] 
arr2 = [5, 6, 7, 8,9] 
interSection(arr1,arr2) 