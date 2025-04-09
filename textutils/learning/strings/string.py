name = 'praveen kumar'  # String to perform various operations on
methodlist = []         # List to store results of operations

# Perform various string operations and assign results to variables a to p
a = len(name)                         # a: Length of the string → 13
b = name[2]                           # b: Character at index 2 → 'a'
c = name.capitalize()                 # c: Capitalizes first letter → 'Praveen kumar'
d = name.title()                      # d: Capitalizes first letter of each word → 'Praveen Kumar'
e = name[0:5:2]                       # e: Slice from index 0 to 5 with step 2 → 'pae'
f = name[::-1]                        # f: Reversed string → 'ramuk neevarp'
g = name.swapcase()                   # g: Swap case → 'PRAVEEN KUMAR'
h = name.lower()                      # h: Convert all letters to lowercase → 'praveen kumar'
i = name.upper()                      # i: Convert all letters to uppercase → 'PRAVEEN KUMAR'
j = name.replace("a", "g")            # j: Replace 'a' with 'g' → 'prgveen kumgr'
k = name.isalnum()                    # k: Checks if all characters are alphanumeric → False (space is not alphanumeric)
l = name.isnumeric()                  # l: Checks if string is numeric → False
m = name.endswith('r')                # m: Checks if string ends with 'r' → True
n = name.startswith('a')              # n: Checks if string starts with 'a' → False
o = name.split(" ")                   # o: Splits string by space into a list → ['praveen', 'kumar']
p = "_".join(name.split(" "))         # p: Joins words with '_' → 'praveen_kumar'

# Append all values to methodlist in alphabetical order of variable names
methodlist.extend([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p])

print(methodlist)  # Print the final list of results
