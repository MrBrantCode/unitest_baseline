"""
QUESTION:
Write a function `total_match(lst1, lst2)` that accepts two lists of strings and returns the list that has the total number of characters (excluding spaces) less than or equal to the other list, while maintaining the original order of elements. The function should remove duplicate strings from both lists (case-insensitive) and consider only the first occurrence of each string. If the two lists have the same number of characters, return the first list. If either list has more than 50% numeric characters in their strings, return an empty list.
"""

def total_match(lst1, lst2):
    """
    Compare two lists of strings and return the list with fewer total characters (excluding spaces).
    
    Remove duplicates from both lists (case-insensitive) and consider only the first occurrence of each string.
    If the lists have the same number of characters, return the first list.
    If either list has more than 50% numeric characters in their strings, return an empty list.
    """
    def remove_duplicates(lst):
        result = []
        for item in lst:
            if item.lower() not in [x.lower() for x in result]:
                result.append(item)
        return result

    def char_count(lst):
        count = 0
        for item in lst:
            count += sum(1 for c in item if c != ' ')
        return count

    def numeric_percent(lst):
        count = 0
        total_chars = 0
        for item in lst:
            for c in item:
                total_chars += 1
                if c.isdigit():
                    count += 1
        return (count / total_chars) * 100 if total_chars > 0 else 0

    lst1, lst2 = remove_duplicates(lst1), remove_duplicates(lst2)

    if (numeric_percent(lst1) > 50) or (numeric_percent(lst2) > 50):
        return []

    count1, count2 = char_count(lst1), char_count(lst2)

    return lst1 if count1 <= count2 else lst2