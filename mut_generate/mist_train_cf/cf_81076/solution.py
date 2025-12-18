"""
QUESTION:
Write a function `find_combinations` that accepts a list of characters and returns all possible combinations of these characters. The function should then be used to generate all possible palindromes from the given character list. The function should return a list of all palindromic combinations.
"""

def find_combinations(chars):
    # base case
    if len(chars) == 0:
        return ['']
    else:
        result = []
        for s in find_combinations(chars[1:]):
            for i in range(len(s)+1):
                result.append(s[:i] + chars[0] + s[i:])
        return result