"""
QUESTION:
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false. 


Each letter in the magazine string can only be used once in your ransom note.


Note:
You may assume that both strings contain only lowercase letters.



canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

def can_construct(ransom_note: str, magazine: str) -> bool:
    # Convert the ransom note into a set of unique characters
    ransom_set = set(ransom_note)
    
    # Check if each character in the ransom note can be matched by the magazine
    for char in ransom_set:
        if ransom_note.count(char) > magazine.count(char):
            return False
    
    return True