"""
QUESTION:
Create a function named `total_match` that takes two lists of strings as input, `lst1` and `lst2`. Return the list with a lesser or equal aggregate of characters throughout its strings, excluding spaces. Remove duplicate strings from the output while preserving the original order of elements, and disregard case during string comparison. If both lists have the same character count, return the first list.
"""

def total_match(lst1, lst2):
    # Removing spaces and changing case to lower for string comparison
    cleaned_lst1 = [str.replace(' ', '').lower() for str in lst1]
    cleaned_lst2 = [str.replace(' ', '').lower() for str in lst2]

    # Checking and removing recurring strings in the lists
    seen = set()
    unique_lst1 = [string for string in lst1 if string.lower() not in seen and not seen.add(string.lower())]

    # Calculating count of characters in cleaned lists
    count_lst1 = sum([len(str) for str in cleaned_lst1])
    count_lst2 = sum([len(str) for str in cleaned_lst2])

    # Checking which list has lesser or equal count of characters
    if count_lst1 <= count_lst2:
        return unique_lst1
    else:
        seen = set()
        unique_lst2 = [string for string in lst2 if string.lower() not in seen and not seen.add(string.lower())]
        return unique_lst2