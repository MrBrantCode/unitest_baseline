"""
QUESTION:
Write a function `unusual_addition(lst)` that takes a list of strings `lst` where each string contains only numerical characters. The function should return a list of strings, where each string in the output list contains the total count of odd numbers squared in the corresponding input string.
"""

def unusual_addition(lst: list) -> list:
    """
    Given a list consisting only of strings with numerical characters, return a list.
    Each string in the output list contains the total count of odd numbers squared in the corresponding input string.
    """ 
    results = []

    for string in lst:
        total_odd = 0

        # Count number of odd numbers within the string
        for char in string:
            if int(char) % 2 != 0:
                total_odd += 1

        # Square of count
        total_odd_squared = total_odd ** 2

        # Append the total count of odd numbers squared to the result list
        results.append(str(total_odd_squared))

    return results