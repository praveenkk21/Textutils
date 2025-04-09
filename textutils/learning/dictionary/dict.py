'''
Dictionary Characteristics:
- key-value paired
- mutable
- unordered (till Python 3.7; ordered from 3.7+)
- dynamic
'''

# Initial dictionary
my_dict = {
    "name": "praveen",
    "course": "python",
    "marks": 100,
    "outcome": ["ai", "ml", "webdev"]
}
print("Initial dictionary:", my_dict)

# Add new key
my_dict["sirname"] = 'b'
print("After adding 'sirname':", my_dict)

# Update value
my_dict["marks"] = 90
print("After updating 'marks':", my_dict)

# Delete a key
del my_dict["sirname"]
print("After deleting 'sirname':", my_dict)

# Access with get()
a = my_dict.get('course')
print("Get 'course':", a)

# Get all keys
b = my_dict.keys()
print("Keys:", list(b))

# Get all values
c = my_dict.values()
print("Values:", list(c))

# Get all items
d = my_dict.items()
print("Items:", list(d))

# Pop a specific key
e = my_dict.pop('marks')
print("Popped 'marks':", e)
print("After popping 'marks':", my_dict)

# Pop last inserted item
f = my_dict.popitem()
print("Last popped item:", f)
print("After popitem():", my_dict)

# Iterating over dictionary
print("Iterating keys (method 1):")
for i in my_dict:
    print(i)

print("Iterating keys (method 2):")
for i in my_dict.keys():
    print(i)

print("Iterating values:")
for i in my_dict.values():
    print(i)

# Clear the dictionary
my_dict.clear()
print("After clear():", my_dict)
