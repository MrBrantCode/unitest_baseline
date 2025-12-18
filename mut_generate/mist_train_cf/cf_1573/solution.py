"""
QUESTION:
Create a function `total_divisible_by_2_and_3(numbers)` that calculates the sum of all unique elements in the input list `numbers` that are divisible by both 2 and 3. If no such elements are found, return -1.
"""

def total_divisible_by_2_and_3(numbers):
    # Remove duplicates from the list
    numbers = list(set(numbers))
    
    # Initialize the total to 0
    total = 0
    
    # Variable to keep track if any element is divisible by both 2 and 3
    found = False
    
    # Iterate over the elements in the list
    for num in numbers:
        # Check if the element is divisible by both 2 and 3
        if num % 2 == 0 and num % 3 == 0:
            # Add the element to the total
            total += num
            found = True
    
    # Check if any element was found
    if found:
        return total
    else:
        return -1