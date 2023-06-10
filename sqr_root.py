# Calculate the square root of a number using the Newton-Raphson method.
# fine a function to calculate the square root of a number
def calculate_square_root(num, precision=0.00001): # default precision is 0.00001
    # Check if the number is negative
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    
    guess = num / 2  # Initial guess
    
    # Loop until the difference between the current guess and the previous guess is less than the precision
    while abs(guess**2 - num) > precision:
        guess = (guess + num / guess) / 2
        
    return guess

# Take user input for the number
num = float(input("Enter a number: "))

# Calculate the square root
sqrt = calculate_square_root(num)

# Print the result
print(f"The square root of {num} is: {sqrt}")