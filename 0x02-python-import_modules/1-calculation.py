#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    
from calculator_1 import add, subtract, multiply, divide as div

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", div(a, b))
