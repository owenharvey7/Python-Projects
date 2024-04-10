# 8
# String Manipulation Challenge:
# Create a program that counts the occurrences of a specific letter in a given string.

# Explain Program
print("This program will count the occurrences of a specific letter in a given string.\n")


def count_letter(string, letter):
    count = 0
    for i in string:
        if i == letter:
            count += 1
    return count


key = False
# Loop so the user can enter multiple strings to check.
while not key:
    try:
        # Ask the user for a string to check.
        string = input("Enter a string: ")
        # Ask the user for a letter to count.
        letter = input("Enter a letter to count: ")
        print(f"The letter '{letter}' appears {count_letter(string, letter)} times in the string '{string}'.")
        print()
    except:
        # If an error occurs, display an error message.
        print("An error occurred.")
        print()
    else:
        # Ask the user if they want to check another string.
        while True:
            try:
                check = input("Would you like to check another string? (y/n): ")
                print()
            except:
                print("An error occurred.")
                print()
            else:
                if check.lower() == "y":
                    break
                elif check.lower() == "n":
                    key = True
                    # Goodbye message.
                    print("Goodbye!")
                    break
                else:
                    # error message for invalid input.
                    print("You must enter 'y' or 'n'.")
                    print()
