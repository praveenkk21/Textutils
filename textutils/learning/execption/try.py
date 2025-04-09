# Example of try-except-finally

try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is:", result)

except ZeroDivisionError:
    # This block runs if a ZeroDivisionError occurs
    print("❌ You can't divide by zero!")

except:
    # This block runs if input is not a valid integer
    print("❌ Please enter a valid number!")

finally:
    # This block always runs, no matter what
    print("✅ Execution finished (finally block).")
