"""
QUESTION:
Write a function `reverse_words` that takes a list of characters representing a sentence of words and reverses the order of the words (not characters) in it. The function should run in O(N) time and use O(1) space complexity, where N is the number of characters in the sentence.
"""

def reverse_words(arr):
    # Reverse the whole array
    def reverse_array(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse_array(0, len(arr) - 1)

    # Reverse individual words
    start = 0
    for end in range(len(arr)):
        if arr[end] == ' ':  
            reverse_array(start, end - 1)  
            start = end + 1  
    # This is for reversing the last word, which isn't followed by a space
    reverse_array(start, len(arr) - 1)

    return "".join(arr)