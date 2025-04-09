# Generator function
# A generator is a type of function that remembers its state 
# and yields values one by one using the yield keyword.
def count_up_to(n):
    i = 1
    while i <= n:
        yield i      # Pause and return i
        i += 1       # Resume from here next time


# Using the generator
for num in count_up_to(5):
    print(num)
