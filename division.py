# Division Program

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the second number is not zero
if num2 != 0:
    # Divide the first number by the second
    result = num1 / num2
    print("The result of dividing {} by {} is: {}".format(num1, num2, result))
else:
    print("Error: Cannot divide by zero. Please enter a non-zero second number.")
