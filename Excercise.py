# Python script to calculate the area of a rectangle

# Function to calculate the area
def calculate_area(length, width):
    area = length * width
    return area

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area using the function
area = calculate_area(length, width)

# Print the result
print("The area of the rectangle is:", area)
