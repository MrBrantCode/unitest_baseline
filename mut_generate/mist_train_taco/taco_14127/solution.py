"""
QUESTION:
In this Kata, you will be given a string and your task is to return the most valuable character. The value of a character is the difference between the index of its last occurrence and the index of its first occurrence. Return the character that has the highest value. If there is a tie, return the alphabetically lowest character. `[For Golang return rune]`

All inputs will be lower case. 

```
For example:
solve('a') = 'a'
solve('ab') = 'a'. Last occurrence is equal to first occurrence of each character. Return lexicographically lowest.
solve("axyzxyz") = 'x'
```

More examples in test cases. Good luck!
"""

def most_valuable_character(st: str) -> str:
    # Calculate the value of each character as the difference between its last and first occurrence indices
    char_values = [(st.rfind(c) - st.find(c), c) for c in set(st)]
    
    # Sort the characters first by their value (descending), then by their lexicographical order (ascending)
    sorted_chars = sorted(char_values, key=lambda x: (-x[0], x[1]))
    
    # Return the character with the highest value (or the lexicographically lowest in case of a tie)
    return sorted_chars[0][1]