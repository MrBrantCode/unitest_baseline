"""
QUESTION:
Implement the `find_longest_palindrome` function, which takes a string as input and returns the longest palindrome within the string that starts and ends with the same letter. The function should have a time complexity of O(n) and space complexity of O(n), where n is the length of the input string. The input string may contain any printable ASCII characters.
"""

def find_longest_palindrome(string):
    # Modify the string
    modified_string = '#' + '#'.join(string) + '#'
    n = len(modified_string)

    # Initialize variables
    P = [0] * n
    C = 0
    R = 0

    # Iterate through the modified string
    for i in range(n):
        j = 2 * C - i

        # Set the initial value of P[i]
        if i < R:
            P[i] = min(R - i, P[j])

        # Attempt to expand the palindrome
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and modified_string[i + P[i] + 1] == modified_string[i - P[i] - 1]:
            P[i] += 1

        # Update C and R if necessary
        if i + P[i] > R:
            C = i
            R = i + P[i]

    # Find the longest palindrome
    max_length = max(P)
    center_index = P.index(max_length)
    start_index = (center_index - max_length) // 2
    end_index = start_index + max_length - 1

    return string[start_index:end_index+1]