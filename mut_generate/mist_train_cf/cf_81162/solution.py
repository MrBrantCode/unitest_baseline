"""
QUESTION:
Write a function `lengthy_text(arr, k)` that takes an array of strings `arr` and an integer `k` as input and returns the longest string in `arr` with a length of at most `k` characters. If no such string exists, return "No valid text found".
"""

def lengthy_text(arr, k):
    # Filtering out texts from array that have number of characters no more than k.
    valid_texts = [text for text in arr if len(text) <= k]
    if not valid_texts:
        return "No valid text found"
    
    # Sorting the valid texts by their lengths in descending order and return the first one.
    most_lengthy_text = sorted(valid_texts, key=len, reverse=True)
    
    return most_lengthy_text[0]