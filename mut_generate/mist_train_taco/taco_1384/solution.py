"""
QUESTION:
## Task

Create a function that given a sequence of strings, groups the elements that can be obtained by rotating others, ignoring upper or lower cases. 

In the event that an element appears more than once in the input sequence, only one of them will be taken into account for the result, discarding the rest. 

## Input

Sequence of strings. Valid characters for those strings are uppercase and lowercase characters from the alphabet and whitespaces.

## Output

Sequence of elements. Each element is the group of inputs that can be obtained by rotating the strings. 

Sort the elements of each group alphabetically. 

Sort the groups descendingly by size and in the case of a tie, by the first element of the group alphabetically.

## Examples

```python
['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris', 'Okyot'] --> [['Kyoto', 'Okyot', 'Tokyo'], ['Donlon', 'London'], ['Paris'], ['Rome']]

['Rome', 'Rome', 'Rome', 'Donlon', 'London'] --> [['Donlon', 'London'], ['Rome']]

[] --> []
```
"""

def group_cities(seq):
    def normalize(s):
        return ''.join(sorted(s.lower()))
    
    unique_seq = list(dict.fromkeys(seq))
    groups = {}
    
    for city in unique_seq:
        normalized = normalize(city)
        if normalized not in groups:
            groups[normalized] = []
        groups[normalized].append(city)
    
    result = [sorted(group) for group in groups.values()]
    result.sort(key=lambda x: (-len(x), x[0].lower()))
    
    return result