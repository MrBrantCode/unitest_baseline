"""
QUESTION:
Create two functions, `how_many_times` and `count_subsequences`, that calculate the occurrences of a given character subsequence in a string. The `how_many_times` function should consider overlapping occurrences, while the `count_subsequences` function should only count non-overlapping occurrences. The functions should take two parameters: `string` and `substring`, both of type `str`, and return the count of the subsequence as an `int`.
"""

def how_many_times(string: str, substring: str) -> int:
    """ Appraise the count of a specified character subsequence present in the input character sequence, considering interlocked occurrences. """
    return sum(1 for i in range(len(string)) if string.startswith(substring, i))

def count_subsequences(string: str, substring: str) -> int:
    """ Determine the occurrences of a designated character subsequence unveiling as a discrete sequence within the input character sequence. """
    counts = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + len(substring)
            counts += 1
        else:
            break
    return counts