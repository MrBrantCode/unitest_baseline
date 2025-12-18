"""
QUESTION:
Implement a function `total_match` that takes two lists of strings (`lst1` and `lst2`) and returns the list with the total character count in all strings being equal to or lesser than the other list, excluding spaces. The function should maintain the original order within each list, eliminate duplicate strings (case-insensitive), and handle nested lists. If both lists have the same character count, return the first list.
"""

from typing import List, Union

def total_match(lst1: List[Union[str, List[str]]], lst2: List[Union[str, List[str]]]) -> List[Union[str, List[str]]]:
    """
    This function compares two lists of strings and returns the list with the total character count 
    in all strings being equal to or lesser than the other list, excluding spaces. It maintains the 
    original order within each list, eliminates duplicate strings (case-insensitive), and handles 
    nested lists. If both lists have the same character count, it returns the first list.

    Args:
    lst1 (List[Union[str, List[str]]]): The first list of strings.
    lst2 (List[Union[str, List[str]]]): The second list of strings.

    Returns:
    List[Union[str, List[str]]]: The list with the total character count in all strings being equal 
    to or lesser than the other list, excluding spaces.
    """

    # Function to flatten a nested list
    def flatten(lst):
        flat_list = []
        for i in lst:
            if isinstance(i, list):
                flat_list.extend(flatten(i))
            else:
                flat_list.append(i)
        return flat_list

    # Flatten the input lists
    lst1 = flatten(lst1)
    lst2 = flatten(lst2)

    # Calculate the total character count in each list, excluding spaces
    count1 = sum(len(s.replace(" ", "")) for s in lst1)
    count2 = sum(len(s.replace(" ", "")) for s in lst2)

    # If both lists have the same character count, return the first list
    if count1 == count2:
        return lst1

    # Remove duplicates from both lists, preserving the original order and ignoring case
    seen1 = set()
    lst1 = [s for s in lst1 if s.lower() not in seen1 and not seen1.add(s.lower())]
    seen2 = set()
    lst2 = [s for s in lst2 if s.lower() not in seen2 and not seen2.add(s.lower())]

    # Return the list with the total character count in all strings being equal to or lesser than the other list
    return lst1 if count1 <= count2 else lst2