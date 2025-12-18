"""
QUESTION:
Create a function called `uncommon_letter_frequency` that takes a list of strings as input and returns a sorted list based on the frequency of their uncommon letters. The uncommon letters are the ones that appear in only one string of the list, and their frequency is defined as the sum of the ASCII codes of all their occurrences in the string where they appear. The output list should be sorted in ascending order based on the sum of the frequency of the uncommon letters in each string. If two or more strings have the same sum of the frequency of the uncommon letters, sort them in alphabetical order.
"""

def uncommon_letter_frequency(lst):
    uncommon_letters = set()
    freq = {}
    for string in lst:
        for c in set(string):
            if all(string.count(c) == lst[i].count(c) for i in range(len(lst)) if c in lst[i]) and string.count(c) == 1:
                uncommon_letters.add(c)
                if c in freq:
                    freq[c] += ord(c)
                else:
                    freq[c] = ord(c)

    return sorted(lst, key=lambda x: sum([freq[c] for c in set(x) if c in uncommon_letters]) or x)