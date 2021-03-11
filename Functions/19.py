#Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce
fib = lambda n: reduce(lambda x, y: x+[x[-1]+x[-2]], range(n-1), [0, 1])

print(fib(10))