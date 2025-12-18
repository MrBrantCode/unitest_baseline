"""
QUESTION:
Given an array of integers 'arr' and a predefined limit of unique element changes, determine the smallest number of elements that need modification to form a palindrome. Each adjustment allows transformation of a single element to any other number. The function should take two parameters: 'arr' (the array of integers) and 'limit' (the predefined limit of unique element changes).
"""

def entrance(arr, limit):
    n = len(arr)
    stack = []

    p1 = 0
    p2 = n - 1

    changes = 0
    while p1 <= p2:
        if arr[p1] != arr[p2]:
            if limit:
                arr[p1 if arr[p1] < arr[p2] else p2] = max(arr[p1], arr[p2])
                changes += 1
                limit -= 1
            else:
                while stack and stack[-1] < min(arr[p1], arr[p2]):
                    stack.pop()
                    changes += 1
                arr[p1 if arr[p1] > arr[p2] else p2] = stack.pop()
        else:
            stack.append(arr[p1])

        p1 += 1
        p2 -= 1

    return changes