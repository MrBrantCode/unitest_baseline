"""
QUESTION:
In this kata you are given an array to sort but you're expected to start sorting from a specific position of the array (in ascending order) and optionally you're given the number of items to sort.

#### Examples:

```python
sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 2) //=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
sect_sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5) //=> [9, 7, 1, 2, 3, 4, 5, 8, 6]
```

#### Documentation:

```python
sect_sort(array, start, length);
```

- array - array to sort
- start - position to begin sorting
- length - number of items to sort (optional)

if the **length** argument is not passed or is zero, you sort all items to the right of the start postiton in the array
"""

def sort_section(array, start, length=0):
    """
    Sorts a specific section of the array starting from a given position.

    Parameters:
    array (list): The array to be sorted.
    start (int): The position in the array from which to start sorting.
    length (int, optional): The number of items to sort. If not provided or zero, sort all items to the right of the start position.

    Returns:
    list: A new list with the specified section sorted in ascending order.
    """
    end = start + length if length else len(array)
    return array[:start] + sorted(array[start:end]) + array[end:]