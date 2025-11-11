# https://github.com/kmendicino/Lab10-KM-JP
# Partner 1: Kate Mendicino
# Partner 2: Jingjing Peng

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, base):
    if a <= 0:
        raise ValueError("Logarithm argument must be > 0")
    if base <= 0 or base == 1:
        raise ValueError("Invalid logarithm base")
    return math.log(a, base)

def exp(a, b):
    return a ** b

def hypotenuse(a, b):
    return math.hypot(a, b)

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)
