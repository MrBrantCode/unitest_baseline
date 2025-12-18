"""
QUESTION:
Create a function named `advanced_monotonic` that takes a list of elements and a boolean value `strict` (defaulting to `False`) as parameters. The function should return `True` if the list elements, after conversion to float, are either monotonically increasing or decreasing, considering the `strict` condition. If any element in the list cannot be converted to a float, the function should return `False`.
"""

def advanced_monotonic(lst: list, strict: bool = False) -> bool:
    try:
        lst = [float(i) for i in lst]
    except ValueError:
        return False

    if strict:
        return all(x<y for x, y in zip(lst, lst[1:])) or all(x>y for x, y in zip(lst, lst[1:]))
    else:
        return all(x<=y for x, y in zip(lst, lst[1:])) or all(x>=y for x, y in zip(lst, lst[1:]))