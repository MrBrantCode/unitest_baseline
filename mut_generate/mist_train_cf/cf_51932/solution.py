"""
QUESTION:
Create a function called `get_positive_sort_eliminate_duplicates` that takes a list of integers as input and returns a list of positive unique numbers from the input list, sorted in ascending order. The function should not use built-in functions like `sort()` or `sorted()`. Additionally, create an auxiliary function within `get_positive_sort_eliminate_duplicates` to sort and eliminate duplicates.
"""

def get_positive_sort_eliminate_duplicates(lst: list):
    """Return only positive unique numbers from the list, sorted in ascending order."""
    
    def swap_remove_duplicates(numbers):
        size = len(numbers)
        for i in range(size):
            for j in range(0, size-i-1):
                if numbers[j] == numbers[j+1]: # Remove duplicates
                    numbers = numbers[:j] + numbers[j+1:]
                elif numbers[j] > numbers[j+1]: # Swap if the element found is greater than the next element
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers

    positive_num = [num for num in lst if num > 0]
    
    return swap_remove_duplicates(positive_num)