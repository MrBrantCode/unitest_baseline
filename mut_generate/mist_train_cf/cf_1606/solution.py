"""
QUESTION:
Create a function `filterAndSortDescending(lst, criteria)` that filters out elements in an array `lst` that do not meet a given criteria and returns the remaining elements in descending order. The function should take the array `lst` and the criteria `criteria` as parameters. The input array will contain at most 10^5 elements and the elements can be integers ranging from -10^9 to 10^9. The function should use a sorting algorithm with a time complexity of O(n log n) and remove any duplicate elements that meet the criteria.
"""

def filterAndSortDescending(lst, criteria):
    filtered = [elem for elem in lst if criteria(elem)]
    filtered.sort(reverse=True)
    return sorted(list(set(filtered)), reverse=True)