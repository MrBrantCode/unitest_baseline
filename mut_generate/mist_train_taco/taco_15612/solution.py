"""
QUESTION:
Write a method that takes a string as an argument and groups the number of time each character appears in the string as a hash sorted by the highest number of occurrences.

The characters should be sorted alphabetically e.g:

```python
get_char_count("cba") == {1: ["a", "b", "c"]}
```

You should ignore spaces, special characters and count uppercase letters as lowercase ones.

For example: 
```python
get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}
get_char_count("Hello. Hello? HELLO!")  ==  {6: ["l"], 3: ["e", "h", "o"]}
get_char_count("aaa...bb...c!")         ==  {3: ["a"], 2: ["b"], 1: ["c"]}
get_char_count("abc123")                ==  {1: ["1", "2", "3", "a", "b", "c"]}
get_char_count("aaabbbccc")             ==  {3: ["a", "b", "c"]}
```
"""

def get_char_count(s: str) -> dict:
    # Initialize an empty dictionary to store character counts
    counts = {}
    
    # Iterate over each character in the string, converting to lowercase and ignoring non-alphanumeric characters
    for c in (c.lower() for c in s if c.isalnum()):
        # Increment the count for the character or initialize it to 1 if it doesn't exist
        counts[c] = counts.get(c, 0) + 1
    
    # Initialize an empty dictionary to store the result
    result = {}
    
    # Iterate over the counts dictionary to populate the result dictionary
    for char, count in counts.items():
        # If the count is already a key in the result dictionary, append the character to the list
        # Otherwise, create a new list with the character
        if count in result:
            result[count].append(char)
        else:
            result[count] = [char]
    
    # Sort the characters in each list alphabetically
    for count in result:
        result[count].sort()
    
    return result