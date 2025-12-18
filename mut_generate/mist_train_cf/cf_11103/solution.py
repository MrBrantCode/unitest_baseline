"""
QUESTION:
Write a function `is_palindrome` that determines if a given array is a palindrome. The array can contain both integers and strings. The function must ignore any non-alphanumeric characters and case sensitivity. If the array has an odd length, the middle element can be any value, but if the array has an even length, all elements must be the same value. The function must return True if the array is a palindrome and False otherwise.
"""

def is_palindrome(arr):
    clean_arr = [str(x).lower() for x in arr if str(x).isalnum()]
    
    if len(clean_arr) % 2 == 0:
        return all(x == clean_arr[0] for x in clean_arr)
    else:
        return clean_arr == clean_arr[::-1]