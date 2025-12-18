"""
QUESTION:
Implement a function `search_letter(letters, target)` where `letters` is a list of sorted uppercase letters and `target` is an uppercase letter. The function should return the largest element in `letters` that is smaller than `target`. If no such element exists, the function should return the last element in `letters` (considering wrap around, i.e., the largest letter in the list that is smaller than the target letter when the list is circularly arranged). The length of `letters` is in the range [2, 10000] and contains at least 2 unique letters.
"""

def search_letter(letters, target):
    left, right = 0, len(letters)
    while left < right:
        mid = (left + right) // 2
        if letters[mid] < target:
            left = mid + 1
        else:
            right = mid
    return letters[left - 1] if left != 0 else letters[-1]