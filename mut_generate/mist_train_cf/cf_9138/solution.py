"""
QUESTION:
Implement a function called `lexicographical_sort` that takes a list of words as input and returns a new list with the words sorted in lexicographical order, ignoring case and without duplicates, without using any built-in sorting functions or libraries.
"""

def lexicographical_sort(words):
    words = list(set(words))  
    for i in range(len(words)):
        words[i] = words[i].lower()  
        
    n = len(words)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]  
    
    return words