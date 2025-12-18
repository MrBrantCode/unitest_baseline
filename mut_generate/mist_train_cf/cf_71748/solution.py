"""
QUESTION:
Write a function named `counter` that takes a string as input and returns a dictionary with three keys: "total", "vowels", and "consonants". The value of each key should be another dictionary containing the frequency of each letter (case sensitive) in the corresponding category. The function should consider 'a' and 'A' as separate characters and count the occurrence of each vowel and consonant separately. The function should only count alphabetic characters.
"""

def counter(string):
    vowels = 'aeiouAEIOU'
    counts = {"total": {}, "vowels": {}, "consonants": {}}
    
    for c in string:
        if c.isalpha():  
            if c in counts["total"]:
                counts["total"][c] += 1
            else:
                counts["total"][c] = 1
            
            if c in vowels:
                if c in counts["vowels"]:
                    counts["vowels"][c] += 1
                else:
                    counts["vowels"][c] = 1
            else:
                if c in counts["consonants"]:
                    counts["consonants"][c] += 1
                else:
                    counts["consonants"][c] = 1
    return counts