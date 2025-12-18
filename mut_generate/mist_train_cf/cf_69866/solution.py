"""
QUESTION:
Implement a function `customized_split(array)` that takes an array of non-negative integers and returns a new array according to the following rules:

- Distribute the elements into three sections ("even_section", "odd_section", "diff_section") based on the sum of the first and penultimate number of the array: 
  - If the sum is even, group even elements into "even_section" and odd elements into "odd_section".
  - If the sum is odd, append all elements into "diff_section".
- Reorganize the elements in each section based on the sum of the first and penultimate numbers: 
  - If the sum is divisible by 6, sort in ascending order.
  - If the sum is divisible by 4 but not by 6, sort in reverse order.
  - Otherwise, sort even elements in ascending order and keep odd elements in their original positions.
- Return the sections combined in the order of "even_section", "odd_section", "diff_section".

The function should not modify the original array. If the array has less than two elements, return the original array.
"""

def customized_split(array):
    """
    This function takes an array of non-negative integers, categorizes them into three sections based on certain rules,
    reorganizes the elements in each section, and returns the combined sections.

    Parameters:
    array (list): A list of non-negative integers.

    Returns:
    list: A new list with the elements categorized and reorganized according to the rules.
    """
    
    # Check array length
    if len(array) < 2:
        return array

    first = array[0]
    penultimate = array[-2]
    sum_value = first + penultimate
    is_even_sum = sum_value % 2 == 0
    is_sum_divisible_by_6 = sum_value % 6 == 0
    is_sum_divisible_by_4 = sum_value % 4 == 0

    even_section = []
    odd_section = []
    diff_section = []

    for num in array:
        is_even = num % 2 == 0
        if is_even:
            even_section.append(num)
        elif is_even_sum:
            odd_section.append(num)
        else:
            diff_section.append(num)

    if is_sum_divisible_by_6:
        even_section.sort()
        odd_section.sort()
        diff_section.sort()
    elif is_sum_divisible_by_4:
        even_section.sort(reverse=True)
        odd_section.sort(reverse=True)
        diff_section.sort(reverse=True)
    else:
        even_section.sort()
        
    return even_section + odd_section + diff_section