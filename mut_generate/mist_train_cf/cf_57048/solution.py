"""
QUESTION:
Write a function total_match that accepts two lists of strings, lst1 and lst2, and returns the list that has the total number of characters (excluding spaces) less than or equal to the other list. The function should remove duplicate strings from both lists, considering only the first occurrence of each string and ignoring case when comparing strings. If the two lists have the same number of characters, return lst1.
"""

def total_match(lst1, lst2):
    # Remove duplicates and ignore case
    lst1 = list(dict.fromkeys([x.lower() for x in lst1]))
    lst2 = list(dict.fromkeys([x.lower() for x in lst2]))

    # Count chars without spaces
    count_lst1 = sum([len(x.replace(' ', '')) for x in lst1])
    count_lst2 = sum([len(x.replace(' ', '')) for x in lst2])

    # Return the list with fewer chars, or lst1 if they are equal
    if count_lst1 <= count_lst2:
        return lst1
    else:
        return lst2