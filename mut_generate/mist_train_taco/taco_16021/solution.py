"""
QUESTION:
Write a function which takes a number and returns the corresponding ASCII char for that value.

Example: 

~~~if-not:java,racket
```
get_char(65) # => 'A'
```
~~~
~~~if:java
~~~
~~~if:racket
~~~

For ASCII table, you can refer to http://www.asciitable.com/
"""

def get_char(c: int) -> str:
    """
    Converts an ASCII value to its corresponding character.

    Parameters:
    c (int): The ASCII value to convert.

    Returns:
    str: The character corresponding to the given ASCII value.
    """
    return chr(c)