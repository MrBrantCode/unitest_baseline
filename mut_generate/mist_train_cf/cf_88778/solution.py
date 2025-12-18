"""
QUESTION:
Write a function `remove_duplicates_and_sort` that takes a string of lowercase letters as input, removes any duplicate characters in-place without using extra space, and sorts the remaining characters in ascending order. The function should return the resulting string.
"""

def remove_duplicates_and_sort(s):
    s = list(s)  # convert the string to a list for in-place modification
    n = len(s)
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]  # swap characters
    
    i = 0
    while i < n-1:  # changed the condition to n-1 to avoid index out of range
        if s[i] == s[i+1]:  # check for duplicate characters
            s.pop(i)  # remove duplicate character by using the pop() function
            n -= 1  # decrease the length of the string
        else:
            i += 1
    
    return ''.join(s)