"""
QUESTION:
Develop a function `compare_and_analyze_lists` that takes two lists of integers, `list1` and `list2`, as input. The function should identify the mutual elements in both lists, the unique elements in each list, the sum of these unique elements, and the count of each mutual element's occurrences in both lists. The function should return the mutual elements, unique elements in each list, their sums, and the counts of mutual elements. Note that the input lists may contain duplicate elements.
"""

def compare_and_analyze_lists(list1, list2):
    """
    This function compares two lists of integers and returns the mutual elements, 
    unique elements in each list, their sums, and the counts of mutual elements.

    Parameters:
    list1 (list): The first list of integers.
    list2 (list): The second list of integers.

    Returns:
    dict: A dictionary containing mutual elements, unique elements in each list, 
          their sums, and the counts of mutual elements.
    """

    # Identify mutual elements
    mutual_elements = list(set(list1) & set(list2))
    
    # Identify unique elements in list1
    unique_elements_list1 = list(set(list1) - set(list2))
    
    # Identify unique elements in list2
    unique_elements_list2 = list(set(list2) - set(list1))
    
    # Sum of unique elements in list1
    sum_unique_list1 = sum(unique_elements_list1)
    
    # Sum of unique elements in list2
    sum_unique_list2 = sum(unique_elements_list2)
    
    # Counting how many times each mutual element appeared in both lists
    mutual_counts = {}
    for e in mutual_elements:
        mutual_counts[e] = (list1.count(e), list2.count(e))

    return {
        "mutual_elements": mutual_elements,
        "unique_elements_list1": unique_elements_list1,
        "unique_elements_list2": unique_elements_list2,
        "sum_unique_list1": sum_unique_list1,
        "sum_unique_list2": sum_unique_list2,
        "mutual_counts": mutual_counts
    }