"""
QUESTION:
Christmas is coming, and Santa has a long list to go through, to find who deserves presents for the big day. Go through a list of children, and return a list containing every child who appeared on Santa's list. Do not add any child more than once. Output should be sorted.
~~~if:java
For java, use Lists.
~~~

Comparison should be case sensitive and the returned list should contain only one copy of each name: `"Sam"` and `"sam"` are different, but `"sAm"` and `"sAm"` are not.
"""

def find_unique_children(santas_list, children):
    """
    Returns a sorted list of unique children who appear in both Santa's list and the children's list.

    Parameters:
    santas_list (list of str): A list of names on Santa's list.
    children (list of str): A list of names of children eligible for presents.

    Returns:
    list of str: A sorted list of unique names that appear in both lists.
    """
    return sorted(set(santas_list) & set(children))