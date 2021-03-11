#Write a Python program to find the first appearance of the substring 
#'not' and 'poor' from a given string,
#if 'not' follows the 'poor', 
#replace the whole 'not'...'poor' substring with 'good'.
#Return the resulting string.

#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'

string = 'The lyrics is not that poor!'

notS = string.find('not')  
poorS = string.find('poor')

if notS>0 and poorS>0 and poorS>notS:
    p = string[:notS] + "good!"
else:
    p = string

print(p)