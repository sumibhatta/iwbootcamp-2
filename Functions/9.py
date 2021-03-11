#Write a Python function that takes a number as a parameter
#and check the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1
#and that has no positive divisors other than 1 and itself.

def primeOrNot(num):
    if(num ==1 or num == 2 ):
        return True
    elif(num<=1 or num%2 == 0 or num%3 == 0):
        return False

    i = 5
    while i**2 <= num:
        if (num%i == 0 or num % (i + 2) == 0):
            return False
        i += 6
    return True

print(primeOrNot(11))
