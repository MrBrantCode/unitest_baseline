"""
QUESTION:
Write a function called `compare_lists` that takes two lists, `list1` and `list2`, as input and returns a dictionary with mutual elements as keys and their counts in both lists as values. The function should include error handling to catch any exceptions that may occur.
"""

def entance(list1, list2):
    try:
        # Create dictionaries based off lists with elements as keys and count as values
        dict1 = {i: list1.count(i) for i in list1}
        dict2 = {i: list2.count(i) for i in list2}

        # Check mutual elements from dict1 to dict2 by exploring keys
        mutual_elements = {i: (dict1[i], dict2[i]) for i in dict1 if i in dict2}

        return mutual_elements
    except Exception as e:
        return "Error occurred: " + str(e)