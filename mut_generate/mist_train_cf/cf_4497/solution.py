"""
QUESTION:
Create a function `unique_concatenation` that takes two strings as input and returns their concatenation with unique characters, sorted in ascending order. The function must implement its own sorting algorithm and have a time complexity of O(nlogn) and a space complexity of O(n), where n is the total number of unique characters in both input strings.
"""

def unique_concatenation(str1, str2):
    unique_chars = set()
    for char in str1:
        unique_chars.add(char)
    for char in str2:
        unique_chars.add(char)
    
    sorted_chars = list(unique_chars)
    n = len(sorted_chars)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = sorted_chars[i]
            j = i
            while j >= gap and sorted_chars[j - gap] > temp:
                sorted_chars[j] = sorted_chars[j - gap]
                j -= gap
            sorted_chars[j] = temp
        gap //= 2
    
    return ''.join(sorted_chars)