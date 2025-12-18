"""
QUESTION:
Write a function `remove_duplicates_and_sort` that takes a string of lowercase letters as input, removes any duplicate characters, and sorts the remaining characters in ascending order. The function must modify the input string in-place without using any extra space.
"""

def remove_duplicates_and_sort(string):
    string = list(string)  
    n = len(string)
    for i in range(n-1):
        for j in range(i+1, n):
            if string[i] > string[j]:
                string[i], string[j] = string[j], string[i]  
    
    i = 0
    while i < n-1:  
        if string[i] == string[i+1]:  
            string.pop(i)  
            n -= 1  
        else:
            i += 1
    
    return ''.join(string)