"""
QUESTION:
Implement a function named `is_happy` that takes a string `s` as input and returns a boolean indicating whether the string is happy or not. A happy string is defined as a string that meets the following conditions: it has a length of at least 3, all consecutive triplets of letters are distinct, every unique letter appears at least twice, there are no back-to-back repeating letters, the total occurrences of each distinct letter is even, and there are no more than two unique letters that appear exactly twice. The function must use a dictionary and a set to ensure that the input string only contains lowercase alphabets.
"""

def is_happy(s):
    
    # Check if string s is too short to be happy.
    if len(s) < 3:
        return False
    
    # Prepare a dictionary to store the frequency of letters and initialize additional variables.
    freq = {}
    repeat = 0
    distinct = set()

    # Iterate over the string s and increment corresponding letter frequency in dict.
    for i in range(len(s)):
        if i > 0 and s[i] == s[i-1]:
            return False # If there are consecutive repeating letters, return False.
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
        distinct.add(s[i]) # Add the letter to the distinct set.
        
    # Iterate over freq dict and count letters having even frequency.
    for k, v in freq.items():
        if v % 2 != 0:
            return False # If a letter frequency is not even, return False.
        if v == 2:
            repeat += 1
            
    # If more than three letters repeat twice each, return False.
    if repeat > 2 or len(distinct) != len(freq):
        return False
        
    # If string s passes all conditions, it is happy.
    for i in range(len(s) - 2):
        if (s[i] == s[i+1] == s[i+2]):
            return False
        if (s[i+1] not in freq or freq[s[i+1]] < 2):
            return False
    return True