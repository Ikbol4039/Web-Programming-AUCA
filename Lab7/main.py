age = 20

if age >= 18:
    print("You are an adult.")

# Output: You are an adult.

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Output: You are not an adult.

age = 20

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Output: You are an adult.

age = 20
ticket = True

if age >= 18:
    if ticket:
        print("You can enter the concert.")

# Output: You can enter the concert.

age = 16

message = "You can drive." if age >= 18 else "You cannot drive."
print(message)

# Output: You cannot drive.

age = 20
ticket = True

if age >= 18 and ticket:
    print("You can enter the concert.")

# Output: You can enter the concert.

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

for i in range(0, 10, 2):
    print(i)

# Output:
# 0
# 2
# 4
# 6
# 8

count = 0

while count < 5:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4

for i in range(10):
    if i == 5:
        break
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

for i in range(5):
    if i == 2:
        continue
    print(i)

# Output:
# 0
# 1
# 3
# 4

for i in range(3):
    print(i)
else:
    print("Loop finished")

# Output:
# 0
# 1
# 2
# Loop finished

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Loop finished")

# Output:
# 0

for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)

# Output:
# i: 0 j: 0
# i: 0 j: 1
# i: 1 j: 0
# i: 1 j: 1
# i: 2 j: 0
# i: 2 j: 1

while True:
    print("This will run forever")
    # ctrl + c что бы остановить 