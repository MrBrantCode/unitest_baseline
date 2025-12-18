"""
QUESTION:
Implement a function called `rotated_search` that takes two parameters: `lst` (a rotated sorted list) and `items` (a list of items to search for in `lst`). The function should return a list of indices corresponding to the positions of each item in `items` within `lst`. If an item is not found, return -1 for that item. Assume `lst` is a list of unique elements and has at least one element. The function should have a time complexity of O(m*log(n)), where m is the number of items and n is the number of elements in `lst`.
"""

def rotated_search(lst, items):
    def find_rotate_index(left, right):
        if lst[left] < lst[right]:
            return 0
        while left <= right:
            pivot = (left + right) // 2
            if lst[pivot] > lst[pivot + 1]:
                return pivot + 1
            else:
                if lst[pivot] < lst[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1
                
    def search(left, right, x):
        while left <= right:
            pivot = (left + right) // 2
            if lst[pivot] == x:
                return pivot
            else:
                if lst[pivot] < x:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1
            
    n = len(lst)
    rotate_index = find_rotate_index(0, n - 1)    
    result = []
    
    for x in items:
        if x >= lst[rotate_index] and x <= lst[n - 1]:
            result.append(search(rotate_index, n - 1, x))
        else:
            result.append(search(0, rotate_index, x))
    
    return result