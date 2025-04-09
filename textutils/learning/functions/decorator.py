# Decorator function p
# A decorator is a special function in Python that can wrap another function to add extra behavior 
# before or after it runs.
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

# Use the decorator
@my_decorator
def say_hello():
    print("Hello!")

say_hello()