"""
QUESTION:
Write a function total_match that accepts two lists of strings (lst1 and lst2) and a boolean parameter unique_chars (default is True). The function should return the list with the lower total character count in the strings (ignoring spaces). If unique_chars is True, only count unique characters in each string. If both lists have the same number of characters, return the first list.
"""

def total_match(lst1, lst2, unique_chars=True):
    def count_chars(lst, unique_chars=True):
        count = 0
        for word in lst:
            if unique_chars:
                count += len(set(word.replace(' ', '')))
            else:
                count += len(word.replace(' ', ''))
        return count

    count1 = count_chars(lst1, unique_chars)
    count2 = count_chars(lst2, unique_chars)

    if count1 <= count2:
        return lst1
    else:
        return lst2