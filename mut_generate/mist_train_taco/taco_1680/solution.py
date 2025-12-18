"""
QUESTION:
Define a method that accepts 2 strings as parameters. The method returns the first string sorted by the second.

```python
sort_string("foos", "of")       == "oofs"
sort_string("string", "gnirts") == "gnirts"
sort_string("banana", "abn")    == "aaabnn"
```

To elaborate, the second string defines the ordering. It is possible that in the second string characters repeat, so you should remove repeating characters, leaving only the first occurrence.

Any character in the first string that does not appear in the second string should be sorted to the end of the result in original order.
"""

def custom_sort_string(s, ordering):
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over each character in the ordering string
    for o in ordering:
        # Append the character from s as many times as it appears in s
        result += o * s.count(o)
        # Remove all occurrences of the character from s
        s = s.replace(o, '')
    
    # Append any remaining characters in s to the result
    return result + s