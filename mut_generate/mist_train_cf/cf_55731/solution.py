"""
QUESTION:
Create a function named `modify_list` that takes a list of integers as input, reverses the list, filters out the odd numbers, and returns the remaining even numbers in non-ascending order. The sorting of even numbers must be implemented without using Python's built-in sort method.
"""

def modify_list(orig_list):
    """
    This function takes a list of integers as input, reverses the list, 
    filters out the odd numbers, and returns the remaining even numbers 
    in non-ascending order.

    The sorting of even numbers is implemented without using Python's 
    built-in sort method.
    """
    def custom_sort(lst):
        """
        Custom implementation of Insertion Sort in descending order.
        """
        for i in range(1, len(lst)):
            key = lst[i]
            j = i-1
            while j >=0 and key > lst[j] :
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = key

    # Reverse the original list
    reverse_list = orig_list[::-1]
    
    # Create a new list that contains only even numbers
    even_list = [num for num in reverse_list if num % 2 == 0]
    
    # Sort the even numbers in non-ascending order
    custom_sort(even_list)
    
    return even_list