"""
QUESTION:
Write a function `list_duplicates_and_uniques(mylist)` that takes a list of numbers as input and returns two lists: one containing the unique numbers in decreasing order and another containing the duplicate numbers in their original order of occurrence.
"""

def list_duplicates_and_uniques(mylist):
    uniques = []
    duplicates = []
    counts = {}

    for number in mylist:
        if number in counts:
            counts[number] += 1
            if counts[number] == 2:
                duplicates.append(number)
        else:
            counts[number] = 1
            uniques.append(number)

    uniques.sort(reverse=True)

    return uniques, duplicates