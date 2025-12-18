"""
QUESTION:
Implement the `get_even_and_merge` function that takes two lists `l1` and `l2` as input and returns a new list containing only the even numbers from both lists, merged and sorted in descending order. The function should include a helper function `merge_and_sort` to handle the merging and sorting of the even numbers from both lists.
"""

def get_even_and_merge(l1: list, l2: list):
    """Return only even numbers from both lists, merged and sorted in descending order."""
    
    def merge_and_sort(m: list, n: list):
        """Merge and sort lists in descending order."""
        merged_list = m + n
        sorted_list = sorted(merged_list, reverse=True)
        return sorted_list

    even_numbers_l1 = [num1 for num1 in l1 if num1 % 2 == 0]
    even_numbers_l2 = [num2 for num2 in l2 if num2 % 2 == 0]

    return merge_and_sort(even_numbers_l1, even_numbers_l2)