import re

text = "My phone numbers are 555-1234, 555-5678, and 555-9999."
phone_numbers = re.findall(r"\d{3}-\d{4}", text)
print("Phone Numbers Found:", phone_numbers)

text1 = "Hello World"
text2 = "Say Hello to everyone"

match1 = re.match(r"Hello", text1)
print("Using re.match() on text1:")
if match1:
    print("Match found:", match1.group())
else:
    print("No match found.")

match2 = re.match(r"Hello", text2)
print("\nUsing re.match() on text2:")
if match2:
    print("Match found:", match2.group())
else:
    print("No match found.")

search_result = re.search(r"Hello", text2)
print("\nUsing re.search() on text2:")
if search_result:
    print("Found:", search_result.group())
else:
    print("Not found.")

text = "There are 12 apples, 30 oranges, and 100 bananas in the basket."
modified_text = re.sub(r"\d+", "NUMBER", text)
print("Modified Text:", modified_text)

email_text = "Contact us at support@example.com or sales@example.org for more info."
emails = re.findall(r"\b\w+@\w+\.\w+\b", email_text)
print("Email Addresses Found:", emails)


sentence = "An apple a day keeps the doctor away. Even elephants enjoy eating."
words = re.findall(r"\b[aeiou]\w*\b", sentence, re.IGNORECASE)
print("Words starting with a vowel:", words)

result_search = re.search(r"\d+", "Order 1234")
print(result_search.group() if result_search else "No match")

result_match = re.match(r"Hello", "Hello World")
print(result_match.group() if result_match else "No match")

result_findall = re.findall(r"\d+", "A12 B34 C56")
print(result_findall)

result_sub = re.sub(r"Java", "Python", "I love Java")
print(result_sub)

result_split = re.split(r"\s+", "Hello World from Python")
print(result_split)