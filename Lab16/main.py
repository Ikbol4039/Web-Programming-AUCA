import json
student = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(student)
print(json_string)

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)
    print(data)

json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
python_object = json.loads(json_data)
print(python_object)

students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]

json_list = json.dumps(students, indent=4)
print(json_list)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

invalid_json = '{"name": "Alice", "age": 25,}'
try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)

student_info = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

serialized = json.dumps(student_info, indent=4)
print("Serialized JSON string:")
print(serialized)

json_string_data = '''
{
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
'''

deserialized = json.loads(json_string_data)
print("Deserialized Python object:")
print(deserialized)

with open("student_data.json", "w") as file:
    json.dump(student_info, file, indent=4)

print("Data has been written to student_data.json")

with open("student_data.json", "r") as file:
    loaded_data = json.load(file)
    print("Data loaded from the JSON file:")
    print(loaded_data)