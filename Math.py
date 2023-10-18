import math

def calculate_circle_area(radius):
    return math.pi * radius**2

# Get user input for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = calculate_circle_area(radius)

# Display the result
print(f"The area of the circle with radius {radius} is: {area}")
