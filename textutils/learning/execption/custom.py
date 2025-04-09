def check_password_strength(password):
    if len(password) < 8:
        raise Exception("Password must be at least 8 characters long.")
    return "Password is strong!"

# Main logic
try:
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    print("✅ Password validation completed.")