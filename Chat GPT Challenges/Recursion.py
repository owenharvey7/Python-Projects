"""
# 14
# Recursion Challenge:
# Write a recursive function to calculate the nth term of the Fibonacci sequence.
# Difficulty: Hard
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nth_term = int(input("Enter the term number: "))

print(f"The {nth_term}th term of the Fibonacci sequence is {fibonacci(nth_term)}")
