'''
Functions:

reusability
modularity
scoping

position based
keyword based
default arguments

'''

def sum(a,b):
    return (a+b)

print(sum(5,10))

def sum(a,b):
    return (a+b)

print(sum(b=5,a=10))

def sum(a=5,b=4):
    return (a+b)

print(sum())