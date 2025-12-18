"""
QUESTION:
Implement a function `count_substrings(s)` that takes a string `s` as input and returns the length of the longest substring without repeating characters. The function should have a time complexity of O(n), where n is the length of `s`.
"""

def length_of_longest_substring(s):
    n = len(s)
    st = set()
    ans, i, j = 0, 0, 0

    while i < n and j < n:
        if s[j] not in st:
            st.add(s[j])
            j += 1
            ans = max(ans, j-i)
        else:
            st.remove(s[i])
            i += 1
    return ans