# Simple calculator that can add, subtract, multiply and divide two numbers
# Author: Sajith Madhusankha
# Created: 2023-06-09
# Try to improve the calculator by adding more functions to it like finding square, cube, squareroot, etc.
    
# This function adds two numbers and return the result 
def add(x, y):
    return x + y

# This function subtracts two numbers and return the result
def subtract(x, y):
    return x - y

# This function multiplies two numbers and return the result
def multiply(x, y):
    return x * y

# This function divides two numbers and return the result
def divide (x, y):
    if y == 0:
        raise ValueError('Can not divide by zero!')
    else:
        return x / y
    
# This function is the main function of the program
def calculator():
    print('Welcome to the calculator!')
    print('Please choose an operation:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')

    # Take input from the user
    choice = input('Enter choice (1/2/3/4): ')

    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    # initiate result variable to store the result
    result = 0

    # Check what operation the user has chosen
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    # If the user has chosen an invalid operation
    else:
        print('Invalid input')
        return
    # Print the result
    print('The result is: ' + str(result))

# Call the calculator function
calculator()