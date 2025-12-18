"""
QUESTION:
Create a function `exchange_with_floats(lst1, lst2)` that determines whether it is possible to swap elements between two lists of numbers (integers and floats) to make the first list contain only even numbers, while keeping the total sum of both lists unchanged. The function should return "YES" if it is achievable and "NO" otherwise.
"""

def exchange_with_floats(lst1, lst2):
    """
    This function determines whether it is possible to swap elements between two lists of numbers 
    (integers and floats) to make the first list contain only even numbers, while keeping the 
    total sum of both lists unchanged.
    
    Args:
        lst1 (list): The first list of numbers.
        lst2 (list): The second list of numbers.
    
    Returns:
        str: "YES" if it is achievable, "NO" otherwise.
    """
    
    # Calculate the sum of both lists
    sum_lst1 = sum(lst1)
    sum_lst2 = sum(lst2)
    
    # Check if the sums of both lists are the same
    if sum_lst1 != sum_lst2:
        return "NO"
    
    # Separate even and odd numbers in both lists
    even_lst1 = [num for num in lst1 if num % 2 == 0]
    odd_lst1 = [num for num in lst1 if num % 2 != 0]
    even_lst2 = [num for num in lst2 if num % 2 == 0]
    odd_lst2 = [num for num in lst2 if num % 2 != 0]
    
    # Check if we have enough even numbers in lst2 to replace all the odd numbers in lst1
    if sum(odd_lst1) > sum(even_lst2):
        return "NO"
    
    # Try to replace odd numbers in lst1 with even numbers from lst2
    for odd_num in odd_lst1:
        for even_num in even_lst2:
            if odd_num <= even_num:
                even_lst2.remove(even_num)
                odd_lst2.append(odd_num)
                break
        else:
            return "NO"
    
    return "YES"