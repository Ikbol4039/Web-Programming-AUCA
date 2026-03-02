from datetime import datetime, timedelta
import calendar
import time

now = datetime.now()
print("Current date and time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

specific_date = datetime(2023, 12, 25, 10, 30, 0)
print("Specific Date:", specific_date)

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

date_string = "2025-02-01 14:30:45"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Date Object:", parsed_date)

future_date = now + timedelta(days=7)
past_date = now - timedelta(days=3)
print("Future Date:", future_date)
print("Past Date:", past_date)

event_date = datetime(2025, 12, 31)
difference = event_date - now
print("Days until event:", difference.days)

print(calendar.month(2025, 2))

seconds = 5
for i in range(seconds, 0, -1):
    print("Time remaining:", i, "seconds")
    time.sleep(1)
print("Time's up!")

start_time = time.time()
time.sleep(0.5)
end_time = time.time()
print("Execution Time:", end_time - start_time)

current = datetime.now()
formatted = current.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatted)

new_year = datetime(current.year, 12, 31)
remaining = new_year - current
print("Days until New Year's Eve:", remaining.days)

countdown_seconds = 10
end_time = datetime.now() + timedelta(seconds=countdown_seconds)

while datetime.now() < end_time:
    remaining_time = end_time - datetime.now()
    print("Time remaining:", remaining_time.seconds, "seconds")
    time.sleep(1)

print("Timer finished!")

year = 2025
month = 3

print("Mon Tue Wed Thu Fri Sat Sun")

first_day = datetime(year, month, 1)
start_weekday = first_day.weekday()

if month == 12:
    next_month = datetime(year + 1, 1, 1)
else:
    next_month = datetime(year, month + 1, 1)

last_day = (next_month - timedelta(days=1)).day

print("    " * start_weekday, end="")

for day in range(1, last_day + 1):
    print(f"{day:>3}", end=" ")
    if (start_weekday + day) % 7 == 0:
        print()

print()