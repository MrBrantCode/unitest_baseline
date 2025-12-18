"""
QUESTION:
Implement a function `camelMatch(queries, pattern)` that takes in a list of strings `queries` and a string `pattern`, and returns a list of booleans where the i-th boolean is True if and only if the i-th query matches the pattern. A query matches the pattern if it can be formed by inserting lowercase letters into the pattern, without breaking the camelcase rule (i.e., a lowercase letter cannot follow an uppercase letter within the same word). The length of the queries and pattern is at most 100, and they only consist of lowercase and uppercase English letters.
"""

def camelMatch(queries, pattern):
    def is_subsequence(q, p):
        i, j = 0, 0
        while i < len(q) and j < len(p):
            if q[i] == p[j]:
                j += 1
            elif q[i].isupper():
                return False
            i += 1
        if j < len(p):
            return False
        while i < len(q):
            if q[i].isupper():
                return False
            i += 1
        return True

    return [is_subsequence(q, pattern) for q in queries]