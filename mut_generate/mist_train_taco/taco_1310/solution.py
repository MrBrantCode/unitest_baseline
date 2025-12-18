"""
QUESTION:
Write a function 

`titleToNumber(title) or title_to_number(title) or titleToNb title ...`

(depending on the language)

that given a column title as it appears in an Excel sheet, returns its corresponding column number. All column titles will be uppercase.

Examples:
```
titleTonumber('A') === 1
titleTonumber('Z') === 26
titleTonumber('AA') === 27
```
"""

def title_to_number(title: str) -> int:
    ret = 0
    for i in title:
        ret = ret * 26 + ord(i) - 64
    return ret