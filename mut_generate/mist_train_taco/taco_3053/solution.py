"""
QUESTION:
The function must return the sequence of titles that match the string passed as an argument. 

```if:javascript
TITLES is a preloaded sequence of strings. 
```

```python
titles = ['Rocky 1', 'Rocky 2', 'My Little Poney']
search(titles, 'ock') --> ['Rocky 1', 'Rocky 2']
```

But the function return some weird result and skip some of the matching results.

Does the function have special movie taste? 

Let's figure out !
"""

def search_titles(titles, term):
    """
    Returns a list of titles that match the given search term.

    Parameters:
    - titles (list of str): A list of strings representing the titles to be searched.
    - term (str): A string representing the search term to be matched in the titles.

    Returns:
    - list of str: A list of titles that contain the search term.
    """
    return list(filter(lambda title: term.lower() in title.lower(), titles))