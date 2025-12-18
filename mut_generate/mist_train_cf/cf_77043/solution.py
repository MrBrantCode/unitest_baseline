"""
QUESTION:
Write a function `find_palindrome_substrings` that takes a string `input_string` as input and returns a tuple containing a list of distinct palindromic substrings in the string and their count. The function should consider all possible substrings of the input string, including single characters, and identify which ones are palindromes. The function should return a tuple where the first element is a list of distinct palindromic substrings in the string, and the second element is the count of these substrings. The list of substrings should be sorted alphabetically.
"""

def find_palindrome_substrings(input_string: str):
    """
    Given a string of text as input, the task is to identify each unique palindromic
    substring within the provided text.
    The function returns a list containing a set of distinct palindromic substrings and their count.
    """
    
    # Initialize a boolean DP array
    n = len(input_string)
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome, hence initialize dp[i][i] to True
    for i in range(n):
        dp[i][i] = True
    
    str_set = set(input_string)  # Initiate a set to hold all distinct palindromic substrings
    
    # Traverse for all possible substrings of length greater than 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            end = i + l
            if l == 2:  # Special case for substrings of length 2
                dp[i][end - 1] = input_string[i] == input_string[end - 1]
            else:
                dp[i][end - 1] = dp[i + 1][end - 2] and input_string[i] == input_string[end - 1]
            
            # Whenever we find a palindrome substring, we add it to our set
            if dp[i][end - 1]:
                str_set.add(input_string[i:end])
    
    # Returning the distinct palindromic substrings and their count
    return sorted(list(str_set)), len(str_set)