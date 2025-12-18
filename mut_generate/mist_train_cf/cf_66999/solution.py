"""
QUESTION:
Write a function `beautySum(s: str) -> int` that calculates the sum of the beauty of all substrings with unique characters in a given string `s`. The beauty of a string is the difference between the frequency of the most frequent character and the least frequent character. The string `s` consists of only lowercase English letters and has a length between 1 and 500.
"""

def beautySum(s: str) -> int:
    total_sum = 0
    for width in range(1, len(s)+1):
        for start in range(len(s)-width+1):
            substring = s[start:start+width]
            if len(substring) == len(set(substring)):
                counts = []
                for char in set(substring):
                    counts.append(substring.count(char))
                total_sum += max(counts) - min(counts)
    return total_sum