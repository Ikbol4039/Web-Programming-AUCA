import math
radius = 5
area = math.pi * math.pow(radius, 2)
print("Area of the circle:", area)

import random
names = ["Alice", "Bob", "Charlie", "David"]
winner = random.choice(names)
print("The winner is:", winner)


import datetime
now = datetime.datetime.now()
print("Current date and time:", now)

specific_date = datetime.date(2024, 1, 1)
print("Specific date:", specific_date)

future_date = now + datetime.timedelta(days=7)
print("Date after 7 days:", future_date)


from math import sqrt
print(sqrt(16))


import math as m
print(m.pi)


from random import *
print(randint(1, 10))

import requests
response = requests.get("https://api.github.com")
print(response.status_code)


# Example using matplotlib (after installing)

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()


# Example using flask (after installing)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()