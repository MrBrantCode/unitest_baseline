"""
QUESTION:
Create a function called `truncate_string` that truncates a given string to display only the first 'n' characters. The function should handle cases where 'n' is greater than the length of the string and also cases where the string is empty. The function should return the truncated string. If 'n' is not a number, the function should return an error message.
"""

def truncate_string(string, n):
    """
    Truncates a given string to display only the first 'n' characters.

    Args:
    string (str): The input string.
    n (int): The number of characters to truncate to.

    Returns:
    str: The truncated string, or an error message if 'n' is not a number.
    """
    try:
        n = int(n)
        if len(string) > n:
            return string[:n]
        else:
            return string
    except ValueError:
        return "Error: n must be a number."
    except Exception as e:
        return "An error occurred: {0}".format(e)