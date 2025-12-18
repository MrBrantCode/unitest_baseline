"""
QUESTION:
Create a function called `sort_list_with_duplicates` that takes two parameters: a list of integers and a string representing the sort order ("ascending" or "descending"). The function should sort the list in the specified order, remove any duplicate elements, and return the sorted list without duplicates. The function should have a time complexity of O(nlogn).
"""

def sort_list_with_duplicates(given_list, sort_order):
    sorted_list = sorted(set(given_list))
    if sort_order == "descending":
        sorted_list.reverse()
    return sorted_list