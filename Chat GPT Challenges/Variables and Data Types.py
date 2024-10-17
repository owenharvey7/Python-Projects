"""
# 2
# Variables and Data Types Challenge:
# Calculate the area of a rectangle using variables for length and width.
# Difficulty: Easy
"""

# Explain program
print("This program will find the area of any rectangle or square given the length and width.\n")

# Get length and width from the user:
length = input("Enter the length of your rectangle in inches: ")
width = input("Enter the width of your rectangle in inches: ")

# Calculate area:
area = float(length) * float(width)

# Display area:
print("The area of your rectangle is " + str(area) + " inches squared.")
