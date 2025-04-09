'''
List Characteristics:
- ordered
- mutable
- dynamic
- heterogeneous
'''

# Original list
my_lst = [1, 2, 3, True]
print("Original my_lst:", my_lst)

lst = my_lst.copy()           # Copy of the list
print("Copied list lst:", lst)

lst_2 = my_lst                # Reference to the same original list
print("Reference list lst_2 (same as my_lst):", lst_2)

# List operations
lst[0] = 'praveen'            # Replace first element with 'praveen'
print("After replacing first element with 'praveen':", lst)

lst[0:3] = [23, 34, 56]       # Replace slice with new elements
print("After replacing first three elements:", lst)

lst * 2                       # Repeat the list (no effect unless reassigned)
print("After lst * 2 (no change in original):", lst * 2 )

lst.append(2)                 # Append 2
print("After append(2):", lst)

lst.extend(lst_2)            # Extend with lst_2 (which is my_lst, now cleared later)
print("After extend with lst_2 (my_lst):", lst)

lst.insert(1, 'kumar')       # Insert 'kumar' at index 1
print("After insert 'kumar' at index 1:", lst)

lst.remove(34)               # Remove first occurrence of 34
print("After remove(34):", lst)

d = lst.pop(2)               # Pop item at index 2
print("Popped element at index 2:", d)
print("After pop(2):", lst)

lst_2.clear()                # Clear my_lst and lst_2
print("After clear() on lst_2 (and my_lst):", lst_2)
print("lst after lst_2.clear():", lst)

# Index and count
try:
    e = lst.index('praveen')     # Find index of 'praveen'
except:
    e = "not found"
print("Index of 'praveen':", e)

f = lst.count(2)             # Count of 2s
print("Count of 2s:", f)

# Sorting
g = lst.copy()
print("Copy before sorting:", g)
try:
    g.sort()
    h = g
except:
    h = "Sorting failed due to incompatible types"
print("Sorted list or error:", h)

# Min and max
try:
    i = min(lst)
except:
    i = "Min failed due to incompatible types"
print("Min value or error:", i)

try:
    j = max(lst)
except:
    j = "Max failed due to incompatible types"
print("Max value or error:", j)

lst.reverse()
k = lst
print("Reversed list:", k)

# Set operations
s1 = set([1, 2, 3])
print("Set s1:", s1)

s2 = set([3, 4, 5])
print("Set s2:", s2)

l = s1.intersection(s2)
print("Intersection of s1 and s2:", l)

# Nested list
m = [s1, lst, ['a', 'd']]
print("Nested list:", m)

# List comprehension
n = [i**2 for i in range(1, 6)]
print("Squares from 1 to 5:", n)

'''
Tuples:
1. Immutable
2. Heterogeneous
3. Defined with ( )
Only limited operations like len, min, max, and count apply
'''
