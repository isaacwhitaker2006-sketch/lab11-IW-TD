#https://github.com/isaacwhitaker2006-sketch/lab11-IW-TD/blob/main/calculator.py
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except TypeError:
        raise TypeError

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
def logarithm(a, b):
    if a <= 0 or a == 1 or  b <= 0:
        raise ValueError
    return math.log(b) / math.log(a)
def exp(a, b):
    return a ** b


