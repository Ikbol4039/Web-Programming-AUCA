import math
# Create a variable name and assign your name to it.
# Create two numeric variables and perform addition, subtraction, multiplication, and division.
# Swap the values of two variables without using a temporary variable.
# Create a constant for the value of pi and calculate the area of a circle with radius 5.

#1st task part3
name = "Ikbol"
print("Name:", name)
#2nd task part3
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
#3rd task part3
x, y = 5, 10
x, y = y, x
print("After swapping: x=", x, ", y=", y)
#4nd task part4
PI = math.pi
radius = 5
area = PI * (radius ** 2)
print("Area:", area)

# Lab Exercise for Students
# Write a program to:
# Take your name and age as input.
# Print a sentence using the entered values.
# Create a program that:
# Takes three numbers as input.
# Prints their sum, average, and product.

#1st task part4 Basic Syntax in Python. Input/Output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and my age is {age} years old")
#2nd task part4 Basic Syntax in Python. Input/Output
a, b, c = map(int, input("Enter three numbers: ").split())
total = a + b + c
average = total / 3
product = a * b * c
print(f"Sum: {total}, Average: {average}, Product: {product}")

#Line comment

"""
This is a multi line
comments
"""

x = 10 #This is an inline comment