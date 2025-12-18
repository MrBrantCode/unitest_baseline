"""
QUESTION:
Write a function `maxUniqueSplit(s)` that takes a string `s` as input and returns the maximum number of unique substrings that `s` can be split into, with the following constraints:

*   The concatenation of the substrings forms the original string.
*   All substrings are unique.
*   Each substring must start with a vowel (a, e, i, o, u).
*   The length of `s` is between 1 and 16 (inclusive).
*   `s` contains only lowercase English letters.
"""

def maxUniqueSplit(s):
    def search(start, seen):
        if start == len(s):
            return 0
        ans = -1
        for end in range(start+1, len(s)+1):
            sub = s[start:end]
            if sub[0] in vowels and sub not in seen:
                seen.add(sub)
                nextSearch = search(end, seen)
                if nextSearch != -1:
                    ans = max(ans, 1 + nextSearch)
                seen.remove(sub)
        return ans if ans != -1 else 0

    vowels = set(['a', 'e', 'i', 'o', 'u'])
    return search(0, set())