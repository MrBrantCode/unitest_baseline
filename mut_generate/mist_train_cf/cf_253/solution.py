"""
QUESTION:
Write a function `bubble_sort(strings)` that sorts a list of strings in alphabetical order, ignoring case sensitivity and handling strings with special characters and numbers based on their ASCII values. The function should implement a sorting algorithm with a time complexity of O(n^2) and should be stable, meaning that the relative order of equal elements is preserved. The function should use only a constant amount of extra space and should not use any built-in sorting functions or libraries.
"""

def bubble_sort(strings):
    n = len(strings)
    for i in range(n):
        # Flag to check if any swapping is done in this pass
        swapped = False
        
        for j in range(0, n-i-1):
            # Convert strings to lowercase for case insensitivity
            string1 = strings[j].lower()
            string2 = strings[j+1].lower()
            
            # Compare ASCII values of characters to handle special characters/numbers
            for k in range(min(len(string1), len(string2))):
                if ord(string1[k]) > ord(string2[k]):
                    strings[j], strings[j+1] = strings[j+1], strings[j]
                    swapped = True
                    break
                elif ord(string1[k]) < ord(string2[k]):
                    break
            
            # Handle case where one string is a prefix of the other
            if not swapped and len(string1) > len(string2):
                strings[j], strings[j+1] = strings[j+1], strings[j]
                swapped = True
        
        # If no swapping is done in this pass, the list is already sorted
        if not swapped:
            break
    
    return strings