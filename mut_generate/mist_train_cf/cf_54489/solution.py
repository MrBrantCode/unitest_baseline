"""
QUESTION:
Implement the function find_common_elements_and_freq(groupA, groupB) to determine the overlap or common elements between two collections, groupA and groupB, and their frequency. groupA and groupB can contain different types of data. The function should consider integer 3 and floating-point 3.0 as the same, as well as string representations of the same numeric values.
"""

def find_common_elements_and_freq(groupA, groupB):
    '''Find common elements and their frequencies across two groups.'''

    def normalize_value(value):
        '''Extract numeric value if possible, else return as is.'''
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except ValueError:
            pass
        return value

    def count_elements(group):
        '''Create a dictionary with counts of normalized elements.'''
        counts = {}
        for ele in group:
            value = normalize_value(ele)
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1
        return counts

    countsA = count_elements(groupA)
    countsB = count_elements(groupB)

    common_elements = set(countsA.keys()) & set(countsB.keys())
    result = {}
    for ele in common_elements:
        result[ele] = {"Frequency in groupA": countsA[ele], "Frequency in groupB": countsB[ele]}
    return result