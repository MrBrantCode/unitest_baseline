"""
QUESTION:
Challenge:
Given two null-terminated strings in the arguments "string" and "prefix", determine if "string" starts with the "prefix" string. Return 1 (or any other "truthy" value) if true, 0 if false.

Example:
```
startsWith("hello world!", "hello"); // should return 1.
startsWith("hello world!", "HELLO"); // should return 0.
startsWith("nowai", "nowaisir"); // should return 0.
```

Addendum:
For this problem, an empty "prefix" string should always return 1 (true) for any value of "string".

If the length of the "prefix" string is greater than the length of the "string", return 0.

The check should be case-sensitive, i.e. startsWith("hello", "HE") should return 0, whereas startsWith("hello", "he") should return 1.

The length of the "string" as well as the "prefix" can be defined by the formula: 0 <= length < +Infinity

No characters should be ignored and/or omitted during the test, e.g. whitespace characters should not be ignored.
"""

def starts_with(string: str, prefix: str) -> int:
    # Handle the special case where prefix is an empty string
    if prefix == "":
        return 1
    
    # Handle the case where the length of prefix is greater than the length of string
    if len(prefix) > len(string):
        return 0
    
    # Check if the string starts with the prefix
    if string.startswith(prefix):
        return 1
    else:
        return 0