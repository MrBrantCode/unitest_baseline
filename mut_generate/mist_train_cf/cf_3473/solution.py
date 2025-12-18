"""
QUESTION:
Implement a function named `reverseList` that takes a list and an integer as input and reverses the order of elements in the list using a recursive algorithm. The list may contain duplicate elements. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(1), without using any extra space apart from the input list itself.
"""

def reverseList(lst, n):
    def reverse(start):
        if start >= n // 2:
            return
        
        lst[start], lst[n - start - 1] = lst[n - start - 1], lst[start]
        
        reverse(start + 1)

    reverse(0)
    return lst