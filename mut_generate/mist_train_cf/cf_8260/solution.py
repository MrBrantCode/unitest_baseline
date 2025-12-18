"""
QUESTION:
Implement a function `filter_even_numbers` that takes a list of integers as input, returns a new list containing the even numbers that are not divisible by 3 or 5, sorted in descending order, and maintains the original order of equal elements. The function should also print the count of even numbers in the input list and the output list. If the input list is empty, print a message indicating that the list is empty and return an empty list.
"""

def filter_even_numbers(numbers):
    # Check if the given list is empty
    if not numbers:
        print("The list is empty")
        return []
    
    # Filter even numbers excluding those divisible by 3 or 5
    even_numbers = [num for num in numbers if num % 2 == 0 and num % 3 != 0 and num % 5 != 0]
    
    # Sort the even numbers in descending order
    even_numbers.sort(reverse=True)
    
    # Print the count of even numbers in the original list and the output list
    print("Count of even numbers in the original list:", sum(1 for num in numbers if num % 2 == 0))
    print("Count of even numbers in the output list:", len(even_numbers))
    
    return even_numbers