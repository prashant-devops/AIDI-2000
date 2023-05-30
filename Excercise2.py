

# Python script to calculate the factorial of a number using recursion

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get user input for the number
num = int(input("Enter a number: "))

# Calculate the factorial using the function
result = factorial(num)

# Print the result
print("The factorial of", num, "is:", result)
