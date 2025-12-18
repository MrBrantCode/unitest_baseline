"""
QUESTION:
Is the number even?

If the numbers is even return `true`. If it's odd, return `false`. 


Oh yeah... the following symbols/commands have been disabled!

 use of ```%```
 use of ```.even?``` in Ruby
 use of ```mod``` in Python
"""

def is_even(n: int) -> bool:
    return not n & 1