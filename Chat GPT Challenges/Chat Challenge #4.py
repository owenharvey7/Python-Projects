# 4
# Conditional Statements Challenge:
# Write a program that determines if a given year is a leap year.

# Explain Program.
print("This program will determine if a given year is a leap year.\n")

# Have user input year.
year = input("Please enter a year: ")

# Create variable and if statements to determine if the year is a leap year.
if float(year) % 4 == 0:
    print("Year", str(year), "is a Leap Year!")
else:
    print("Year", str(year), "is not a Leap Year :(")