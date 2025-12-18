"""
QUESTION:
Implement a function `custom_sort(data)` that takes a list of dictionaries as input where each dictionary contains 'name' and 'location' as keys. The function should sort the input data by 'location' based on a custom lexicographic order defined by the `custom_lexicographic_order(str1, str2)` function. This function compares two strings character by character and returns True if `str1` is lexicographically less than or equal to `str2`, and False otherwise. The `custom_sort` function should return the sorted list of dictionaries.
"""

def custom_lexicographic_order(str1, str2):
    """
    Compare two strings character by character and return True if str1 is lexicographically less than or equal to str2, False otherwise.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
    
    Returns:
        bool: Whether str1 is lexicographically less than or equal to str2.
    """
    i = 0
    while(i < len(str1) and i < len(str2)): 
        if(ord(str1[i]) < ord(str2[i])): 
            return True
        elif(ord(str1[i]) > ord(str2[i])): 
            return False
        i += 1
    return len(str1) <= len(str2) 


def custom_sort(data):
    """
    Sort the input data by 'location' based on a custom lexicographic order.
    
    Args:
        data (list): A list of dictionaries where each dictionary contains 'name' and 'location' as keys.
    
    Returns:
        list: The sorted list of dictionaries.
    """
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if not custom_lexicographic_order(data[j]['location'], data[j + 1]['location']):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data