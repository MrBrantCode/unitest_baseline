"""
QUESTION:
Implement a function `nth_longest_string` that takes a list of strings and an integer `n` as parameters. The function should return the `n`th longest string in the list, where the indexing is 1-based. If `n` is out of range, not an integer, or an error occurs, the function should return an error message.
"""

def nth_longest_string(arr, n):
    try:
        arr.sort(key=len, reverse=True)
        return arr[n-1]
    except IndexError:
        return "The provided index is out of range."
    except TypeError:
        return "The value for 'n' must be an integer."
    except:
        return "An error has occurred."