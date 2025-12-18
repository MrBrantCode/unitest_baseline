"""
QUESTION:
Write a function `minimum_changes_to_palindrome(arr, limit)` that calculates the minimum number of changes required to make the frequency of each element in the array a palindrome, with the restriction that no element can have a frequency greater than the given limit. The function takes two parameters: `arr` (the input array) and `limit` (the maximum allowed frequency of an element).
"""

def minimum_changes_to_palindrome(arr, limit):
    from collections import Counter

    freq_counter = Counter(arr)
    sorted_keys = sorted(freq_counter.keys())
    count = 0

    i = 0
    j = len(sorted_keys) - 1

    while i <= j:
        if freq_counter[sorted_keys[i]] < limit and freq_counter[sorted_keys[j]] < limit:
            count += 2
        elif freq_counter[sorted_keys[i]] < limit:
            count += 1  
        elif freq_counter[sorted_keys[j]] > limit:
            count += 1
        i += 1
        j -= 1

    return count