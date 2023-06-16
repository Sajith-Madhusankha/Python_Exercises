# Unit Converter Program
# Author: Sajith Madhusankha
# Created: 2023/06/16
# Try to add more units and conversions to the program

# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Meters to Feet
def meters_to_feet(meters):
    return meters * 3.281

# Feet to Meters
def feet_to_meters(feet):
    return feet / 3.281

# Kilograms to Pounds
def kilograms_to_pounds(kilograms):
    return kilograms * 2.205

# Pounds to Kilograms
def pounds_to_kilograms(pounds):
    return pounds / 2.205

# Square Meters to Square Feet
def square_meters_to_square_feet(square_meters):
    return square_meters * 10.764

# Square Feet to Square Meters
def square_feet_to_square_meters(square_feet):
    return square_feet / 10.764

# Gigabytes to Terabytes
def gigabytes_to_terabytes(gigabytes):
    return gigabytes / 1024

# Terabytes to Gigabytes
def terabytes_to_gigabytes(terabytes):
    return terabytes * 1024

# Joules to Calories
def joules_to_calories(joules):
    return joules / 4.184

# Calories to Joules
def calories_to_joules(calories):
    return calories * 4.184

# Main Program
print("Unit Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Meters to Feet")
print("4. Feet to Meters")
print("5. Kilograms to Pounds")
print("6. Pounds to Kilograms")
print("7. Square Meters to Square Feet")
print("8. Square Feet to Square Meters")
print("9. Gigabytes to Terabytes")
print("10. Terabytes to Gigabytes")
print("11. Joules to Calories")
print("12. Calories to Joules")

# Get user choice
choice = input("Select conversion type (1-12): ")

# Perform conversion
if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius = {fahrenheit} degrees Fahrenheit")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit = {celsius} degrees Celsius")
elif choice == "3":
    meters = float(input("Enter length in meters: "))
    feet = meters_to_feet(meters)
    print(f"{meters} meters = {feet} feet")
elif choice == "4":
    feet = float(input("Enter length in feet: "))
    meters = feet_to_meters(feet)
    print(f"{feet} feet = {meters} meters")
elif choice == "5":
    kilograms = float(input("Enter weight in kilograms: "))
    pounds = kilograms_to_pounds(kilograms)
    print(f"{kilograms} kilograms = {pounds} pounds")
elif choice == "6":
    pounds = float(input("Enter weight in pounds: "))
    kilograms = pounds_to_kilograms(pounds)
    print(f"{pounds} pounds = {kilograms} kilograms")
elif choice == "7":
    square_meters = float(input("Enter area in square meters: "))
    square_feet = square_meters_to_square_feet(square_meters)
    print(f"{square_meters} square meters = {square_feet} square feet")
elif choice == "8":
    square_feet = float(input("Enter area in square feet: "))
    square_meters = square_feet_to_square_meters(square_feet)
    print(f"{square_feet} square feet = {square_meters} square meters")
elif choice == "9":
    gigabytes = float(input("Enter storage in gigabytes: "))
    terabytes = gigabytes_to_terabytes(gigabytes)
    print(f"{gigabytes} gigabytes = {terabytes} terabytes")
elif choice == "10":
    terabytes = float(input("Enter storage in terabytes: "))
    gigabytes = terabytes_to_gigabytes(terabytes)
    print(f"{terabytes} terabytes = {gigabytes} gigabytes")
elif choice == "11":
    joules = float(input("Enter energy in joules: "))
    calories = joules_to_calories(joules)
    print(f"{joules} joules = {calories} calories")
elif choice == "12":
    calories = float(input("Enter energy in calories: "))
    joules = calories_to_joules(calories)
    print(f"{calories} calories = {joules} joules")

# Invalid choice
else:
    print("Invalid choice.")
