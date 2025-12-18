"""
QUESTION:
Your friend has invited you to a party, and tells you to meet them in the line to get in. The one problem is it's a masked party. Everyone in line is wearing a colored mask, including your friend. Find which people in line could be your friend.

Your friend has told you that he will be wearing a `RED` mask, and has **TWO** other friends with him, both wearing `BLUE` masks.

Input to the function will be an array of strings, each representing a colored mask. For example:
```python
line = ['blue','blue','red','red','blue','green']
```

The output of the function should be the number of people who could possibly be your friend.
```python
friend_find(['blue','blue','red','red','blue','green','chipmunk'])  # return 1
```
"""

def count_possible_friends(line):
    def red_with_2_blues(i, line):
        return any((line[i - 2 + x:i + 1 + x].count('blue') == 2 for x in range(3)))
    
    return sum((p == 'red' and red_with_2_blues(i, line) for (i, p) in enumerate(line)))