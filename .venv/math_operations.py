# Task 1: Perform Basic Mathematical Operations

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing basic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Displaying the results
print("\nAddition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
