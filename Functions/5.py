#Write a Python function to calculate the factorial of a number
#(a non-negative integer).
# The function accepts the number as an argument.

def factorial(num):
    if(num == 1):
        return 1
    return num * factorial(num-1)

print(factorial(6))