# 5
# Loops Challenge:
# Write a program that prints the Fibonacci sequence up to the 10th term using a loop.

# Explain Program
print("This program will print the Fibonacci sequence up to the nth term based on your input.\n")

# Have user input number between 1 - 10.
n = input("How man terms of the Fibonacci sequence would you like to see? Please only select up to 10: ")

# Validate users input
while float(n) > 10:
    n = input("Invalid number, please select a number between 1-10: ")
while float(n) < 0:
    n = input("Invalid number, please select a number between 1-10: ")
print("You entered a number between 1-10!")

# Create the Fibonacci Sequence
n1, n2 = 0, 1
count = 0

# Create while loop to print the sequence

if float(n) == 1:
    print("Fibonacci sequence up to", n, ":")
    print(n1)
else:
    print("Fibonacci sequence up to", n, ":")
    while count < float(n):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

print("The fibonacci sequence has been printed for the", n, "th term. It is ", n1, ".")
