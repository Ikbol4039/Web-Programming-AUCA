def greet():
    print("Hello, World!")

greet()
# Output:Hello, World!

# 2. Function Parameters
def greet(name):
    print("Hello,", name)

greet("Ikbol")
# Output:Hello, Alice

# 3. Default Parameters
def greet(name="Almaz"):
    print("Hello,", name)

greet()
greet("Ali")
# Output: Hello, Guest
# Hello, Bob

# 4. Returning Values
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# Output: 8

# 5. Multiple Return Values
def calculate(a, b):
    return a + b, a - b

sum_result, diff_result = calculate(10, 5)
print("Sum:", sum_result)
print("Difference:", diff_result)
# Output: Sum: 15 Difference: 5

# 6. Variable-Length Arguments
# *args (Positional Arguments)

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))

# Output: 15
# **kwargs (Keyword Arguments)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Alice", age=25)
# Output: name : Alice age : 25

# 7. Lambda Functions
square = lambda x: x * x
print(square(4))

# Output: 16
# Lambda in Sorting

numbers = [(1, 2), (3, 1), (5, 0)]
numbers.sort(key=lambda x: x[1])
print(numbers)
# Output: [(5, 0), (3, 1), (1, 2)]

# 8. Scope of Variables
# Local Scope

def my_function():
    x = 10
    print(x)
my_function()
# Output: 10
# Global Scope

x = 5
def modify():
    global x
    x = 10
modify()
print(x)

# Output: 10
# 9. Recursion (Factorial)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
# Output: 120
# 10. Docstrings

def greet(name):
    """
    This function greets a person by name.
    """
    print("Hello,", name)

print(greet.__doc__)
# Output: This function greets a person by name.