"""
QUESTION:
Given the function name `count_distinct_substrings`, write a function that takes a string `string` as input and returns the number of distinct continuous substrings in the string, where a distinct substring is defined as a substring that does not contain any duplicate characters. The solution must have a time complexity of O(n^2), a space complexity of O(n), and only use constant extra space excluding the input and output variables.
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