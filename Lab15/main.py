import os
import csv

with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python makes file handling easy.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

try:
    with open("newfile.txt", "x") as file:
        file.write("This file was created using x mode.\n")
except FileExistsError:
    print("File already exists.")

with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("Processed line:", line.strip())

data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "22", "Chicago"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}.")

with open("people.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["David", "28", "Houston"])

with open("sample_text.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text for testing file operations.\n")

print("Content has been written to sample_text.txt")

with open("sample_text.txt", "r") as file:
    print("Content read from the file:")
    print(file.read())

people_data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(people_data)

print("Data has been written to people.csv")

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    print("Reading data from the CSV file:")
    for row in reader:
        print(row)

with open("sample_text.txt", "a") as file:
    file.write("This line is appended to the file.\n")

print("Additional text has been appended to sample_text.txt")

with open("sample_text.txt", "r") as file:
    print("Updated content of the file:")
    print(file.read())