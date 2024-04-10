# 7
# Functions Challenge:
# Write a function that checks if a given number is prime.

# Explain Program
print("This program will check if a given number is prime.\n")


def is_prime(num):
    if num <= 1:
        return "Not a prime number."
    else:
        for i in range(2, num):
            if num % i == 0:
                return "Not a prime number."
        return "The number you entered is a prime number."


key = False
# Loop so the user can enter multiple numbers to check if they are prime.
while not key:
    try:
        # Ask the user for a number to check.
        num = int(input("Enter a number: "))
        print(is_prime(num))
        print()
    except ValueError:
        # If the user enters a non-integer, display an error message.
        print("You must enter a number.")
        print()
    except:
        # If an error occurs, display an error message.
        print("An error occurred.")
        print()
    else:
        # Ask the user if they want to check another number.
        while True:
            try:
                check = input("Would you like to check another number? (y/n): ")
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
