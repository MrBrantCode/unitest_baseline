"""
QUESTION:
Write a function named `find_usernames` that takes a list of usernames and a target string as input, and returns a list of usernames that start with the target string. The search should be case-sensitive. The function should not use any external libraries and should have a time complexity of O(n log n) or better.
"""

def find_usernames(usernames, target):
    """
    This function finds and returns a list of usernames that start with the target string.
    
    Args:
    usernames (list): A list of usernames.
    target (str): The target string to search for.

    Returns:
    list: A list of usernames that start with the target string.
    """
    # Sort the list of usernames in alphabetical order
    usernames.sort()

    # Initialize an empty list to store the usernames that match the search criteria
    matches = []

    # Initialize two pointers, left and right, to the beginning and end of the sorted list respectively
    left = 0
    right = len(usernames) - 1

    # Perform binary search
    while left <= right:
        mid = (left + right) // 2
        if usernames[mid].startswith(target):
            # If the username at the mid index starts with the target, add it to the list of matches
            matches.append(usernames[mid])
            # Search for more matches in the rest of the list
            for i in range(mid + 1, len(usernames)):
                if usernames[i].startswith(target):
                    matches.append(usernames[i])
                else:
                    break
            for i in range(mid - 1, -1, -1):
                if usernames[i].startswith(target):
                    matches.append(usernames[i])
                else:
                    break
            break
        elif usernames[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # Return the list of matches
    return matches