import os
import sys

# Hardcoded credentials (Security issue)
USERNAME = "admin"
PASSWORD = "password123"

# Unused variable (Code smell)
unused_variable = "This is never used"

def division(a, b):
    # Division by zero (Potential bug)
    return a / b

def read_file():
    # Ignoring exceptions (Bad practice)
    try:
        with open("config.txt", "r") as file:
            data = file.read()
        return data
    except:
        pass

def unsafe_exec(user_input):
    # Security issue: Using eval (Major vulnerability)
    eval(user_input)

def infinite_loop():
    # Infinite loop (Code smell)
    while True:
        print("Running...")

if __name__ == "__main__":
    print("Starting application...")
    
    # Potentially dangerous use of user input
    user_input = input("Enter command: ")
    unsafe_exec(user_input)

    # Possible division by zero
    print(division(10, 0))

    # Read file without handling specific exceptions
    config_data = read_file()
