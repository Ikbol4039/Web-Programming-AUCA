x = 5 #Integer
y = -1 #Negative integer
z = 0 #zero
print(type(x)) #it will return int

a = 0.5 #positive float
b = -3.4 #negative float
c = 2.5e3 #scientific notation (2.5*10^3)
print(type(a)) #output float

c1 = 3 + 4j   # Complex number
c2 = 2 - 5j   # Another complex number
print(type(c1))   # Output: <class 'complex'>

greeting = "Hello, World!"
name = 'Alice'
print(type(greeting))   # Output: <class 'str'>

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person["name"])   # Output: Alice
print(type(person))     # Output: <class 'dict'>

unique_numbers = {1, 2, 3, 4, 5, 5, 4}  # Duplicate values will be removed
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
print(type(unique_numbers))  # Output: <class 'set'>

frozen_set = frozenset([1, 2, 3])
print(frozen_set)        # Output: frozenset({1, 2, 3})
print(type(frozen_set))  # Output: <class 'frozenset'>

is_active = True
is_admin = False
print(type(is_active))

byte_data = b"hello"  # Byte literal
print(byte_data)       # Output: b'hello'
print(type(byte_data)) # Output: <class 'bytes'>

mutable_bytes = bytearray([65, 66, 67])  # List of ASCII codes
mutable_bytes[0] = 68  # Change first byte
print(mutable_bytes)        # Output: bytearray(b'DBC')
print(type(mutable_bytes))  # Output: <class 'bytearray'>

x1 = "10"
y1 = int(x1)  # Convert string to integer
print(type(y1))  # Output: <class 'int'>

x2 = "3.14"
y2 = float(x2)  # Convert string to float
print(type(y2))  # Output: <class 'float'>

x3 = 100
y3 = str(x3)  # Convert integer to string
print(type(y3))  # Output: <class 'str'>

x4 = "hello"
y4 = list(x4)  # Convert string to list of characters
print(y4)  # Output: ['h', 'e', 'l', 'l', 'o']

# 1. User input for different types
integer_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
string_input = input("Enter a string: ")
print(type(integer_input))  # Output: <class 'int'>
print(type(float_input))    # Output: <class 'float'>
print(type(string_input))   # Output: <class 'str'>

# 2. Type Conversion and Dictionary
text = "123"
number = int(text)          # Convert to integer
number_float = float(number)  # Convert to float
print(type(number))         # Output: <class 'int'>
print(type(number_float))   # Output: <class 'float'>
person = {
    "name": "Bob",
    "age": 30
}
print(person["name"])       # Output: Bob

# 3. Operations on Sets
my_set = {1, 2, 3}
my_set.add(4)               # Add element
my_set.remove(2)            # Remove element
print(3 in my_set)          # Check membership, Output: True