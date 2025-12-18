"""
QUESTION:
The task is very simple.

You must to return pyramids. Given a number ```n```  you print a pyramid with ```n``` floors

For example , given a ```n=4``` you must to print this pyramid:

```
   /\
  /  \
 /    \
/______\ 
   
```

Other example, given a ```n=6``` you must to print this pyramid:

```  
     /\
    /  \
   /    \
  /      \
 /        \
/__________\

```

Another example, given a ```n=10```, you must to print this pyramid:

```
         /\
        /  \
       /    \
      /      \
     /        \
    /          \
   /            \
  /              \
 /                \
/__________________\

```

Note: an extra line feed character is needed at the end of the string. Case `n=0` should so return `"\n"`.
"""

def generate_pyramid(n: int) -> str:
    """
    Generates a pyramid with `n` floors as a string.

    Args:
        n (int): The number of floors in the pyramid.

    Returns:
        str: A string representing the pyramid with `n` floors, including an extra line feed character at the end.
    """
    if n == 0:
        return "\n"
    
    return '\n'.join(('/{}\\'.format(' _'[r == n - 1] * r * 2).center(2 * n).rstrip() for r in range(n))) + '\n'