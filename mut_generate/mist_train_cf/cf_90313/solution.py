"""
QUESTION:
Create a function named `filter_even_numbers` that takes a list of integers as input. The function should return a new list containing the even numbers from the input list that are not divisible by 3 or 5, sorted in descending order while preserving the original order of equal values. If the input list is empty, the function should print a message indicating the list is empty and return an empty list. Additionally, the function should print the total count of even numbers in the original list and the output list.
"""

def filter_even_numbers(numbers):
    # Check if the given list is empty
    if not numbers:
        print("The list is empty")
        return []
    
    # Filter even numbers excluding those divisible by 3 or 5
    even_numbers = [num for num in numbers if num % 2 == 0 and num % 3 != 0 and num % 5 != 0]
    
    # Sort the even numbers in descending order while preserving the original order of equal values
    even_numbers = sorted(even_numbers, reverse=True)
    
    # Print the count of even numbers in the original list and the output list
    even_count_original = len([num for num in numbers if num % 2 == 0])
    print("Count of even numbers in the original list:", even_count_original)
    print("Count of even numbers in the output list:", len(even_numbers))
    
    return even_numbers