"""
QUESTION:
Create a function `uncommon_letter_frequency(lst)` that takes in a list of strings `lst` and returns a sorted list based on the frequency of their uncommon letters. The uncommon letters are the ones that appear in only one string of the list. For each uncommon letter, its frequency is defined as the sum of the ASCII codes of all its occurrences in the string where it appears. The output list should be sorted in ascending order based on the sum of the frequency of the uncommon letters in each string. If two or more strings have the same sum of the frequency of the uncommon letters, sort them in alphabetical order.
"""

def uncommon_letter_frequency(lst):
    uncommon_letters = set()
    freq = {}
    for string in lst:
        for c in set(string):
            if sum([string.count(c) for string in lst]) == 1:
                uncommon_letters.add(c)
                if c in freq:
                    freq[c] += ord(c) * lst.count(string)
                else:
                    freq[c] = ord(c) * lst.count(string)

    return sorted(lst, key=lambda x: sum([freq[c] for c in set(x) if c in uncommon_letters]) or x)