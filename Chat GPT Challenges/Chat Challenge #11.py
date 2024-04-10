# 11
# Exception Handling Challenge:
# Modify the division program to handle different types of exceptions and provide appropriate error messages.

def divide(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return "You cannot divide by zero."
    except ValueError:
        return "You must enter a number."
    except:
        return "An error occurred."

a = input("Enter a number to be divided: ")
b = input("Enter another number (the divisor): ")

print(divide(a, b))