"""
QUESTION:
Create a function `get_even_and_merge` that takes two lists of integers as input and returns a new list containing only the even numbers from both lists, merged and sorted in descending order. The function should not modify the original lists. 

The function should handle lists of any size and content. If a list is empty, the function should still return a valid result. If a list contains non-integer values, the function should ignore these values. 

Implement a helper function `merge_and_sort` to merge and sort the lists.
"""

def get_even_and_merge(l1: list, l2: list):
    """Return only even numbers from both lists, merged and sorted in descending order."""

    def merge_and_sort(m: list, n: list):
        m.extend(n)  # merge the two lists
        m.sort(reverse=True)  # sort the merged list in descending order
        return m

    even_numbers = [num for num in l1 if isinstance(num, int) and num % 2 == 0]  
    even_numbers += [num for num in l2 if isinstance(num, int) and num % 2 == 0]  

    return merge_and_sort(even_numbers, [])  # sort the even_numbers list in descending order