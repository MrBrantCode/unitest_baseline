"""
QUESTION:
Implement a function `is_happy(s, l)` that checks if the input string `s` is 'happy' and exists in the list `l`. A string is 'happy' if it has a length of at least 3, every trio of consecutive letters is unique, every distinct character occurs at least twice, there are no consecutive duplicate letters, and the total count of occurrences for each unique letter is an even number. The function should return `True` if the string is 'happy' and exists in the list, and `False` otherwise.
"""

def is_happy(s, l):
    # Check if string is in list
    if s not in l: 
        return False

    # Check if length of string is at least 3
    if len(s) < 3: 
        return False
        
    # Check if every trio of consecutive letters is unique
    triplets = set()
    for i in range(len(s) - 2):
        triplet = s[i: i + 3]
        if triplet in triplets:
            return False
        triplets.add(triplet)
    
    # Check if every distinct character occurs a minimum of two times
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1   

    # Check if there shouldn't be any consecutive duplicate letters
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            return False
                
    # Check if the total count of occurrences for each unique letter has to be an even number
    for count in char_count.values():
        if count % 2 != 0:
            return False
            
    return True