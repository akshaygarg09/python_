# File: main.py

# Import functions from the custom library
from mylibrary import factorial, is_prime

# Using the factorial function
num = 5
result_factorial = factorial(num)
print(f"The factorial of {num} is: {result_factorial}")

# Using the is_prime function
num = 13
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
