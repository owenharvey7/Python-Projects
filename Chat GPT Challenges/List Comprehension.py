"""
# 13
# List Comprehensions Challenge:
# Use list comprehension to create a list of even numbers from 1 to 20.
# Difficulty: Easy
"""

# Most efficient way to create a list of even numbers from 1 to 20 using list comprehension.
def main():
    even_numbers = [number for number in range(1, 21) if number % 2 == 0]
    print(even_numbers)

main()


# More basic way to create a list of even numbers from 1 to 20 using a for loop.
# Create a list variable to store even numbers.
even = []
# Loop through numbers 1 to 20.
for i in range(1, 21):
    # Check if the number is even.
    if i % 2 == 0:
        # Add number to the list.
        even.append(i)
# Print a list of even numbers.
print("Even numbers between 1 to 20: " + str(even))
