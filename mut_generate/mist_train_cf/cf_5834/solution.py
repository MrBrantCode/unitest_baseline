"""
QUESTION:
Find all duplicates in an array of integers within the range 1 to 10^9 (inclusive) and return them in descending order. The function, `find_duplicates(arr)`, should take an array `arr` as input and must be efficient enough to handle up to 10^12 elements.
"""

def findDuplicates(arr):
    seen = set()
    duplicates = []
    
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    
    duplicates.sort(reverse=True)
    return duplicates