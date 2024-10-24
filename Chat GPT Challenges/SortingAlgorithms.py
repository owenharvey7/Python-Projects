"""
# 20
# Sorting Algorithms Challenge
# Implement a more advanced sorting algorithm (e.g., merge sort) on a list of numbers.
# Difficulty: Hard
"""

# Function to sort a list of numbers using merge sort
def merge_sort(numbers):
    # Base case: If the list is empty or contains only one element, it is already sorted
    if len(numbers) <= 1:
        return numbers
    # Find the middle of the list
    mid = len(numbers) // 2
    # Recursively split the list into two halves
    left_half = merge_sort(numbers[:mid])
    right_half = merge_sort(numbers[mid:])
    # Merge the two halves
    return merge(left_half, right_half)


# Function to merge two sorted lists into one
def merge(left, right):
    # Create a result list
    result = []
    # Iterate over the two lists
    while len(left) > 0 and len(right) > 0:
        # Compare the smallest elements of the two lists
        if left[0] <= right[0]:
            # Add the smallest element of the left list to the result
            result.append(left.pop(0))
        else:
            # Add the smallest element of the right list to the result
            result.append(right.pop(0))
    # Add any remaining elements from the left list to the result
    result.extend(left)
    # Add any remaining elements from the right list to the result
    result.extend(right)
    # Return the sorted list
    return result

def merge_sort(numbers):
    # Base case: If the list is empty or contains only one element, it is already sorted
    if len(numbers) <= 1:
        return numbers
    # Find the middle of the list
    mid = len(numbers) // 2
    # Recursively split the list into two halves
    left_half = merge_sort(numbers[:mid])
    right_half = merge_sort(numbers[mid:])
    # Merge the two halves
    return merge(left_half, right_half)


# Example usage
numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
