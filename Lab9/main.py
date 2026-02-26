#Exception Handling Using try and except
#Example: Handling Different Exceptions Separately
try:
    x = int(input("Enter a number: "))
    print(10/x)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")

#Example: Catching Multiple Exceptions Together
try:
    x = int(input("Enter a number: "))
    print(10/x)
except (ZeroDivisionError, ValueError):
    print("Error: Invalid operation")

#Using else in Exception Handling
try:
    x = int(input("Enter a number: "))
    res = 10/x
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result:", res)

#Usinf finally
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")
    file.close()

#Example: Raising a Built-in Exception
def withdraw(amount, balance):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
try:
    new_baance = withdraw(300, 200)
except ValueError as e:
    print("Error:, {e}")

#Example: Raising NotImplementedError
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses of Shape must implement area")

#Example: Creating and Using a Custom Exception
class NegativeNumberError (Exception):
    def __init__(self, message = "Negative number are not allowed"):
        self.message = message
        super().__init__(self.message)

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return number ** 0.5

try:
    a = int(input("Enter a number: "))
    res = square_root(a)
except NegativeNumberError as e:
    print("Error:, {e}")

#Example: Hierarchy of Custom Exceptions
class ApplicationError(Exception):
    pass
class DatabaseError(ApplicationError):
    pass
class ValidationError(ApplicationError):
    pass
try:
    raise ValidationError("Invalid input")
except ValidationError as e:
    print("Error:, {e}")
except ApplicationError as e:
    print("Error:, {e}")

