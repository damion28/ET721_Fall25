"""
Damion Ally
lab 4, dictionary and cuntions
Sep 10, 2025
"""

print("\n---- Example 1: dictionary ----\n")
# contact dictionary with three different users
contacts = {"Bill": "718-111-222", "Martha": "646-000-3333", "Peter": "212-000-1111"}
print(contacts)

# save the value of a specific key
user1 = contacts["Martha"]
print(f"user's phone number = {user1}")

# add new content to the dictionary
contacts["Anna"] = "646-222-3333"
print(contacts)

# update value of a specific key
contacts["Peter"] = "800-000-0000"
print(contacts)

print("\n---- Example 2: loop through a dictionary ----\n")
# print each key in the dictionary
for i in contacts:
    print(i)

# print each value in the dictionary
for i in contacts:
    print(contacts[i])

# print each key:value set in the dictionary
for i in contacts:
    print(f"{i} = {contacts[i]}")

print("\n---- Example 3: length of a dictionary ----\n")
print(f"Dictionary has {len(contacts)} users")

print("\n---- Example 4: copy a dictionary ----\n")
copy_contact1 = contacts.copy()
copy_contact2 = dict(contacts)
print(copy_contact1)
print(copy_contact2)

print("\n---- Example 5: remove a key:alue pair in a dictionary ----\n")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("\n---- Example 6: add a new key:value pair in a dictionary ----\n")
print(contacts)
contacts.update({"Lucas": "212-111-1111"})
print(contacts)

print("\n---- Example 7: return items, keys, and values in a dictionary ----\n")
print(f"Return items = {contacts.items()}")
print(f"Return keys = {contacts.keys()}")
print(f"Return values = {contacts.values}")

print("\n---- Example 8: dictionary application ----\n")
# store in a dictionary the count of occurency of the words in a phrase
phrase = "to be or not to be"
list_phrase = phrase.split()
# create an empty dictionary
word_count_dict = {}
for word in list_phrase:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

# print result
for word in word_count_dict:
    print(f"'{word}' appears {word_count_dict[word]}")

print("\n---- Exercise ----\n")
users = [
    "peterpan@yahoo.com",
    "annie@hotmail.com",
    "Carl@hotmail.com",
    "martha@gmail.com",
    "cassie@yahoo.com",
    "Josue@hotmail.com",
    "John@hotmail.com",
]

email_count = {"gmail": 0, "hotmail": 0, "yahoo": 0}

for user in users:
    if "gmail" in user:
        email_count["gmail"] += 1
    elif "hotmail" in user:
        email_count["hotmail"] += 1
    elif "yahoo" in user:
        email_count["yahoo"] += 1

for provider in email_count:
    print(f"'{provider}' appears {email_count[provider]}")
