"""
QUESTION:
Write a function `palindrome_analysis(strings)` that takes a list of strings as input and returns information about the palindromic strings in the list. The function should identify the longest palindromic string, the shortest palindromic string, and the average length of all palindromic strings in the list. The function should also handle potential exceptions, such as null entries in the list. Assume the input list has at least one element, but may contain null entries.
"""

def palindrome_analysis(strings):
    """
    Analyze a list of strings for palindromicity.

    Args:
    strings (list): A list of strings.

    Returns:
    dict: A dictionary containing information about the palindromic strings.
    """

    # Filter out null entries from the original list
    strings = [s for s in strings if s is not None]

    # Create a new list of only the palindromes
    palindromes = [s for s in strings if s == s[::-1]]

    if not palindromes:
        return {"error": "No palindromes found."}
    else:
        # Identify the longest and shortest palindrome
        longest_palindrome = max(palindromes, key=len)
        shortest_palindrome = min(palindromes, key=len)
        
        # Calculate the average length of all palindromes
        average_palindrome_length = sum(len(s) for s in palindromes) / len(palindromes)

        return {
            "longest_palindrome": longest_palindrome,
            "shortest_palindrome": shortest_palindrome,
            "average_palindrome_length": average_palindrome_length,
        }