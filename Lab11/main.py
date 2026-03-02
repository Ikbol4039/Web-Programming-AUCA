# Lists Example
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.reverse()
numbers.sort()
print(numbers)

# List Slicing
print(numbers[:3])
print(numbers[-2:])
print(numbers[::-1])

# Dictionary Example
student = {"name": "Alice", "age": 22, "grade": "A"}
student["subject"] = "Math"
student["grade"] = "A+"
student.pop("age")
print(student.keys())
print(student.values())
print(student.items())

# Set Example
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# Tuple Example
colors = ("red", "blue", "green", "red", "yellow")
print(colors.index("green"))
print(colors.count("red"))

# List Methods Demonstration
my_list = [3, 1, 4]
my_list.append(5)
my_list.extend([6, 7])
my_list.insert(1, 10)
my_list.pop(0)
my_list.remove(4)
my_list.sort()
my_list.reverse()
print(my_list.index(10))
print(my_list.count(6))

# Dictionary Methods Demonstration
my_dict = {"a": 1, "b": 2}
print(my_dict.get("a"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.update({"c": 3})
my_dict.pop("b")
my_dict.clear()

# Set Methods Demonstration
my_set = {1, 2, 3}
my_set.add(10)
my_set.remove(2)
my_set.discard(100)
print(my_set.union({5, 6}))
print(my_set.intersection({1, 10}))
print(my_set.difference({1}))
my_set.clear()

# Tuple Methods Demonstration
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))
print(my_tuple.index(3))

# Nested Data Structures
company = {
    "employees": [
        {"name": "Alice", "position": "Manager", "salary": 5000},
        {"name": "Bob", "position": "Developer", "salary": 4000}
    ]
}

company["employees"].append(
    {"name": "Charlie", "position": "Designer", "salary": 3500}
)

for employee in company["employees"]:
    print(employee["name"])