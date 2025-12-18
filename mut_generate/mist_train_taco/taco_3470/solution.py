"""
QUESTION:
Write a function that checks if all the letters in the second string are present in the first one at least once, regardless of how many times they appear:

```
["ab", "aaa"]    =>  true
["trances", "nectar"]    =>  true
["compadres", "DRAPES"]  =>  true
["parses", "parsecs"]    =>  false
```

Function should not be case sensitive, as indicated in example #2. Note: both strings are presented as a **single argument** in the form of an array.
"""

def contains_all_letters(arr):
    # Convert both strings to lowercase to ensure case insensitivity
    main_string = arr[0].lower()
    check_string = arr[1].lower()
    
    # Check if all characters in check_string are in main_string
    return set(check_string).issubset(set(main_string))