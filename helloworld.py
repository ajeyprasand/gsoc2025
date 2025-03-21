import os

# Hardcoded credentials (Security issue)
USERNAME = "admin"
PASSWORD = "password123"

def authenticate(user, pwd):
    if user == USERNAME and pwd == PASSWORD:  # Hardcoded credentials used here
        return "Authentication Successful"
    else:
        return "Authentication Failed"

# Unused variable (Code Smell)
unused_variable = 42

def process_data(data):
    # Inefficient string concatenation in a loop (Performance issue)
    result = ""
    for item in data:
        result += item  # This is inefficient; should use join()
    return result

# Exception not handled properly (Bug)
def divide_numbers(a, b):
    try:
        return a / b
    except:
        print("An error occurred")  # Generic exception handling, not specifying the error type

# Duplicated Code (Code Smell)
def greet_user1(name):
    return f"Hello, {name}!"

def greet_user2(name):
    return f"Hello, {name}!"  # Duplicate function

# Function with too many parameters (Code Smell)
def complex_function(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j

# Dead Code (Code Smell)
def unused_function():
    print("This function is never called")
