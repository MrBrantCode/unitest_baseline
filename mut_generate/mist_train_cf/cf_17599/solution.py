"""
QUESTION:
Write a function called `count_distinct_substrings` that takes a string as input and returns the number of distinct continuous substrings in the string. A distinct substring is defined as a substring that does not contain any duplicate characters. The function must have a time complexity of O(n^2) and a space complexity of O(n). The solution must use only constant extra space (excluding the input and output variables) and cannot use any built-in data structures or libraries for handling strings or arrays. The input string can contain uppercase and lowercase letters, digits, and special characters, and its length n satisfies 1 ≤ n ≤ 10^6.
"""

def count_distinct_substrings(string):
    n = len(string)
    counter = 0
    distinct_set = set()

    left = 0
    right = 0

    while right < n:
        if string[right] not in distinct_set:
            distinct_set.add(string[right])
            counter += (right - left + 1)

        else:
            while string[left] != string[right]:
                distinct_set.remove(string[left])
                left += 1
            left += 1

        right += 1

    return counter