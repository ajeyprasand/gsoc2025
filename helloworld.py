import platform

# Reference to an undefined variable (Bug)
def check_value(x):
    if x > 10:
        result = "High"
    else:
        pass  # 'result' is never assigned in this case
    return result  # Undefined variable error

# Unreachable code (Code Smell)
def always_returns():
    return "Done"
    print("This will never execute")  # Unreachable

# Wrong fields in formatted strings
name = "Alice"
message = "{user} has logged in".format(username=name)  # Incorrect field name

# Type Errors
output_shape = (64, 64, 3)
state_shape = output_shape[1:]  # Correctly assigned as tuple
output_shape = [32, 32, 3]  # Reassigned as list
print(state_shape[0] + output_shape[0])  # Type error: tuple + list

# Wrong argument type
def get_length(value):
    return len(value)  # If an integer is passed, it will throw TypeError

print(get_length(10))  # This will cause a runtime error

# Comparisons that don’t make sense
arch = platform.architecture()
if arch == "64bit":  # 'arch' is a tuple, this comparison is always False
    print("64-bit system detected")

# Ignored return value
warning_msg = "Make sure that your dataset can generate at least "
warning_msg.format(1000)  # The formatted result is discarded

# Unraised exceptions
class CustomException(Exception):
    pass

def risky_function():
    CustomException("Something went wrong")  # Should be 'raise CustomException(...)'

# Calling the functions to demonstrate issues
try:
    print(check_value(5))
except Exception as e:
    print(f"Error: {e}")

always_returns()
risky_function()
