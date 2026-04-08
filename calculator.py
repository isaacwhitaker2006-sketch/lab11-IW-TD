import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
def logarithm(a, b):
    if a <= 0 or a == 1 or  b <= 0:
        raise ValueError
    return math.log(b) / math.log(a)
def exponent(a, b):
    return a ** b


