"""
QUESTION:
Create a function custom_sort(l: list, n: int, m: int, s: str) that takes a list l, two integers n and m, and a string s ('asc' or 'desc') as inputs. The function should return a new list where elements at indices not within the range(n, m) remain the same as in the original list, while elements within the range(n, m) are squared and sorted in the order specified by s. The range(n, m) is inclusive of the nth index but exclusive of the mth index.
"""

def custom_sort(l: list, n: int, m: int, s: str):
    # Generate the squared list subset
    subset = [i**2 for i in l[n:m]]
    # Sort the subset in the correct order
    subset.sort(reverse=(s == 'desc'))
    # Replace the original subset with our new subset
    l[n:m] = subset
    return l