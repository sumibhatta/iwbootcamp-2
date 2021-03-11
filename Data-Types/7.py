#Write a Python function that takes a list of words and 
# returns the length of the longest one.

def longestOne(words):
   return max(words, key=len)


long = longestOne(['python','issssssssssssss','awesomeeeeeeeeeee'])
print(long)