"""
QUESTION:
Create a function `sort_names(names)` that takes in a list of strings `names` representing relative names. The function should return a new list containing only the names that have more than 3 vowels in them, ignoring case when counting vowels. The output list should be sorted in descending order based on the number of vowels in each name. If two names have the same number of vowels, the name that comes first in the input list should come first in the output list. Do not use built-in sorting functions, and achieve a time complexity of O(n^2), where n is the length of the input list.
"""

def sort_names(names):
    def count_vowels(name):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for char in name:
            if char.lower() in vowels:
                count += 1
        return count

    names_with_vowels = []
    for name in names:
        if count_vowels(name) > 3:
            names_with_vowels.append(name)

    for i in range(len(names_with_vowels)):
        max_index = i
        for j in range(i + 1, len(names_with_vowels)):
            if count_vowels(names_with_vowels[j]) > count_vowels(names_with_vowels[max_index]):
                max_index = j
            elif count_vowels(names_with_vowels[j]) == count_vowels(names_with_vowels[max_index]):
                if names.index(names_with_vowels[j]) < names.index(names_with_vowels[max_index]):
                    max_index = j
        names_with_vowels[i], names_with_vowels[max_index] = names_with_vowels[max_index], names_with_vowels[i]

    return names_with_vowels